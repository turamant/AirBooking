from django.db import models

from apps.aircrafts.models import Aircraft


class Seat(models.Model):
    aircraft_code = models.ForeignKey(Aircraft, verbose_name='Код воздушного судна',
                                      on_delete=models.CASCADE, related_name='seats')
    seat_number = models.CharField(verbose_name='номер места', max_length=10)
    fare_conditions = models.CharField(verbose_name='условия тарифа', max_length=100)

    def __str__(self):
        return self.seat_number