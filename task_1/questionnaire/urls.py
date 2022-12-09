from django.urls import path
from questionnaire.views import *


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:id>', TestView.as_view(), name='test'),
    path('<int:id>/questions/', QuestionView.as_view(), name='questions'),
    path('<int:id>/questions/completed/', ComplitedView.as_view(), name='completed'),
]