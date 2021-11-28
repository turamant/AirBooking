from django.db import models


class Aircraft(models.Model):
    aircraft_code = models.CharField(verbose_name='Код воздушного судна',
                                     max_length=6, unique=True)
    model = models.CharField(verbose_name='Модель воздушного судна',
                             max_length=10)
    range = models.CharField(verbose_name='ранг',
                             max_length=10)

    def __str__(self):
        return self.model
