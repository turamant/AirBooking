from django.db import models

from apps.flights.models import Flight
from apps.tickets.models import Ticket


class TicketFlight(models.Model):
    ticket_number = models.ForeignKey(Ticket, verbose_name='Номер билета',
                                      on_delete=models.CASCADE, related_name='ticketflights')
    flight_id = models.ForeignKey(Flight, verbose_name='Рейс',
                                  on_delete=models.CASCADE, related_name='ticketflights')
    fare_conditions = models.CharField(verbose_name='Условия тарифа', max_length=100)
    amount = models.CharField(verbose_name='Количество', max_length=10)

    def __str__(self):
        return self.fare_conditions