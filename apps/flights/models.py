import uuid

from django.db import models

from apps.aircrafts.models import Aircraft


class Flight(models.Model):
    flight_id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    flight_number = models.CharField(verbose_name='Номер рейса', max_length=100, unique=True)
    scheduled_departure = models.CharField(verbose_name='Время вылета по расписанию',
                                          max_length=10)
    scheduled_arrival = models.CharField(verbose_name='Время прилета по расписанию',
                                         max_length=10)
    status = models.CharField(verbose_name='Статус рейса', max_length=10)
    aircraft_code = models.ForeignKey(Aircraft, verbose_name='код воздушного судна',
                                      on_delete=models.CASCADE, related_name='flights')
    actual_departure = models.CharField(verbose_name='Время вылета актуальное',
                                        max_length=10)
    actual_arrival = models.CharField(verbose_name='Время вылета актуальное',
                                        max_length=10)

