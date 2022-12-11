import random
import radar


from random import randrange
from datetime import datetime, timedelta
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse

from cardsmanager.models import *


class HomeView(View):
    template_name = 'cardsmanager/home.html'

    def post(self, request):
        """
        Возвращает отфильтрованный список карт по параметрам
        """
        if request.POST.get('action') == 'card-filter':
            filter_set = {}

            series = request.POST.get("filter-series")
            status = request.POST.get("filter-status") 
            
            release_year = request.POST.get("filter-release-year")
            release_month = request.POST.get("filter-release-month")
            release_day = request.POST.get("filter-release-day")

            end_of_activity_year = request.POST.get("filter-end-activity-year")
            end_of_activity_month = request.POST.get("filter-end-activity-month")
            end_of_activity_day = request.POST.get("filter-end-activity-day")

            if series:
                filter_set['series'] = series

            
            if status != 'All':
                filter_set['status'] = status

            if release_year:
                filter_set['release__year'] = release_year
            if release_month:
                filter_set['release__month'] = release_month
            if release_day:
                filter_set['release__day'] = release_day

            if end_of_activity_year:
                filter_set['end_of_activity__year'] = end_of_activity_year
            if end_of_activity_month:
                filter_set['end_of_activity__month'] = end_of_activity_month
            if end_of_activity_day:
                filter_set['end_of_activity__day'] = end_of_activity_day

            return render(request, self.template_name, {'cards': Card.objects.filter(**filter_set)})


    def get(self, request):
        """
        Отображение всех карт
        """
        return render(request, self.template_name, {'cards': Card.objects.all()})



class CardView(ListView):
    template_name = 'cardsmanager/card.html'

    def get(self, request, id):
        """
        Отображение информации о карте с историей покупок
        """
        card = Card.objects.get(pk=id)
        history = card.history_set.all()
        

        context = {
            'card': card,
            'history': history,
        }

        return render(request, self.template_name, context)


    def post(self, request, id):
        """
        Смена статуса или удаление карты
        """
        card = Card.objects.get(pk=id)

        if request.POST.get('action') == 'status-cahnge':
            if card.status == 'NA':
                card.status = 'AC'
            elif card.status == 'AC':
                card.status = 'NA'
            card.save()
            return redirect(reverse('card', kwargs={'id': id}))

        if request.POST.get('action') == 'status-delete':
            card.delete()
            return redirect(reverse('home'))

        
class CardGenerator(View):
    template_name = 'cardsmanager/generator.html'
    
    def get(self, request):
        return render(request, self.template_name, {})

    def post(self, request):
        
        amount = request.POST.get('generator-amount')
        series = request.POST.get('generator-series')
        end_activity = request.POST.get('generator-end-activity')
        history = request.POST.get('generator-history')

        for i in range(int(amount)):
            
            delta = {
                '1':timedelta(days=30), 
                '6': timedelta(days=180),
                '12': timedelta(days=365)
                }

            release = datetime.now() if not history else radar.random_datetime()
            end_of_activity =  release + delta[end_activity]
            status = 'NA' if not history else 'AC' if datetime.now() < end_of_activity else 'EX'
        
            number = random.randint(10000000000, 999999999999)
            balans = random.randint(0, 1000000)
            
            new_card = Card.objects.create(
                    series = series,
                    number = number,
                    release = release,
                    status = status,
                    balans = balans,
                    end_of_activity = end_of_activity
                )
                
            if history: 
                for j in range(random.randint(2, 10)):
                    debit = random.randint(1, 10000)
                    date = radar.random_datetime(release, end_of_activity)
                    History.objects.create(card=new_card, date=date, debit=debit)

        return redirect(reverse('home'))
