# Generated by Django 4.1.4 on 2022-12-09 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardsmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='date_of_use',
            field=models.DateTimeField(editable=False, verbose_name='Дата и время последнего использования карты'),
        ),
    ]
