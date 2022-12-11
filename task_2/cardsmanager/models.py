from django.db import models


class Card(models.Model):
    STATUS_CHOISES = (
        ('AC', 'activated'),
        ('NA', 'not activated'),
        ('EX' , 'expired'),
    )

    series = models.CharField(max_length=4, verbose_name='Серия карты')
    number = models.CharField(max_length=12, verbose_name='Номер карты')
    balans = models.CharField(max_length=10, verbose_name='Баланс карты')
    release = models.DateTimeField(verbose_name='Дата и время выпуска карты')
    date_of_use = models.DateTimeField(verbose_name='Дата и время последнего использования карты', editable=False, null=True)
    end_of_activity = models.DateTimeField(verbose_name='Дата и время окончания активности карты')
    status = models.CharField(max_length=2, choices=STATUS_CHOISES,  default='NA', verbose_name='Статус карты')

class History(models.Model):
    card = models.ForeignKey(Card, on_delete=models.CASCADE)
    debit = models.CharField(max_length=10, verbose_name='Сумма списания с карты')
    date = models.DateTimeField(verbose_name='Дата и время списания')
