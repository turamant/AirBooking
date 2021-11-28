from django.db import models


class Airport(models.Model):
    airport_code = models.UUIDField(verbose_name='Код аэропорта', max_length=100)
    airport_name = models.CharField(verbose_name='Имя аэропорта', max_length=100)
    city = models.CharField(verbose_name='Город', max_length=100)
    coordinates = models.CharField(verbose_name='Координаты аэропорта', max_length=100)
    timezone = models.CharField(verbose_name='Часовой пояс', max_length=100)

    def __str__(self):
        return self.airport_name










