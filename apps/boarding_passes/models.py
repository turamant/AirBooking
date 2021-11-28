from django.db import models

from apps.flights.models import Flight
from apps.seats.models import Seat
from apps.tickets.models import Ticket


class BoardingPass(models.Model):
    class Meta:
        db_table = 'boardingpasses'

    ticket_number = models.ForeignKey(Ticket, verbose_name='Номер билета',
                                      on_delete=models.CASCADE, related_name='boardingpasses')
    flight_id = models.ForeignKey(Flight, verbose_name='Рейс',
                                  on_delete=models.CASCADE, related_name='boardingpasses')
    boarding_number = models.CharField(verbose_name='Номер посадочного талона', max_length=10)
    seat_number = models.ForeignKey(Seat, verbose_name='Номер места',
                                    on_delete=models.CASCADE, related_name='boardingpasses')

    def __str__(self):
        return self.boarding_number
