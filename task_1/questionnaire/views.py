from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from django.views.generic import ListView, DetailView
from questionnaire.models import *


class HomeView(ListView):
    template_name = 'questionnaire/home.html'
    model = Test
        

class TestView(View):
    template_name = 'questionnaire/test.html'

    def get(self, request, id):

        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        test = Test.objects.get(pk=id)
        test_questions = test.question_set.all()
        
        user_answers = []
        for quest in test_questions:
            if answer := quest.useranswer_set.filter(user=request.user).first() is not None:
                user_answers.append(answer)

        qeustions_info = test_questions.count()
        answers_info = len(user_answers)

        if qeustions_info == answers_info:
            return redirect(reverse('completed', kwargs={'id': id}))
        else:
            context = {
                'header': test.header,
                'questions': qeustions_info ,
                'answers': answers_info,
            }
            return render(request, self.template_name, context)


class QuestionView(View):
    template_name = 'questionnaire/question.html'

    def post(self, request, id):
        
        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        answers_id = request.POST.getlist('user-answer')
        for answer_id in answers_id:
            answer = Answer.objects.get(id=answer_id)
            UserAnswer.objects.create(user=request.user, answer=answer, question=answer.question, test_id=id)

        return redirect(reverse('questions', kwargs={'id': id}))


    def get(self, request, id):       
        
        if not request.user.is_authenticated:
            return redirect(reverse('login'))

        test = Test.objects.get(pk=id)
        questions = test.question_set.all()

        for quest in questions:
            user_answers = quest.useranswer_set.filter(user=request.user).all()
            quest_user_answers = [answer.question for answer in user_answers]

            if quest not in quest_user_answers:
                answers = quest.answer_set.all()

                context = {
                    'header': test.header,
                    'question': quest.question,
                    'answers': answers,
                }
                return render(request, self.template_name, context)

        return redirect(reverse('completed', kwargs={'id': id}))
    

class ComplitedView(View):
    template_name = 'questionnaire/completed.html'

    def get(self, request, id):
        if not request.user.is_authenticated:
            return redirect(reverse('login'))
        
        test = Test.objects.get(pk=id)
        questions = test.question_set.all()
        
        right = 0
        for quest in questions:
            correct_answers_queryset = quest.answer_set.filter(correct=True)

            check_answers = []
            for correct_answer in correct_answers_queryset:
                try:
                    correct_answer.useranswer_set.get(user=request.user)
                    check_answers.append(True)
                except:
                    check_answers.append(False)

            if all(check_answers):
                right += 1

        count = questions.count()
        
        context = {
            'header': test.header,
            'false': count - right,
            'right': right,
            'score': right / count  * 100,
        }
        return render(request, self.template_name, context)

