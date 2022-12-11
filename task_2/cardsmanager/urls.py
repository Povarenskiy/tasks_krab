from django.urls import path
from cardsmanager.views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:id>/', CardView.as_view(), name='card'),
    path('generator/', CardGenerator.as_view(), name='generator')
]