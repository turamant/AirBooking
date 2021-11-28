from django.contrib.auth.models import User
from django.db import models

from apps.bookings.models import Booking
from apps.users.models import Profile


class Ticket(models.Model):
    class Meta:
        db_table = 'tickets'
        ordering = ['ticket_number']

    ticket_number = models.CharField(verbose_name='Номер билета',
                                     max_length=9, unique=True)
    book_ref = models.ForeignKey(Booking, verbose_name='номер брони',
                                 on_delete=models.CASCADE, related_name='tickets')
    passenger_id = models.ForeignKey(User, verbose_name='пассажир с id',
                                     on_delete=models.CASCADE, related_name='tickets')
    passenger_name = models.ForeignKey(Profile, verbose_name='Профиль пассажира',
                                       on_delete=models.CASCADE, related_name='tickets' )
    contact_data = models.TextField(max_length=100)

    def __str__(self):
        return self.ticket_number
