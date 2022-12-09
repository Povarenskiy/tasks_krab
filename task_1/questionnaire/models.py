from django.db import models
from users.models import *


class Test(models.Model):
    header = models.TextField(max_length=255, verbose_name='Заголовок')


class Question(models.Model):
    question = models.TextField(max_length=255, verbose_name='Вопрос')
    test = models.ForeignKey(Test, on_delete=models.CASCADE)


class Answer(models.Model):
    answer = models.TextField(max_length=255, verbose_name='Вариант ответа')
    correct = models.BooleanField(default=False, verbose_name='Верный')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


class UserAnswer(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE) 
    user = models.ForeignKey(User, on_delete=models.CASCADE)


