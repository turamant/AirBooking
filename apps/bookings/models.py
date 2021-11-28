from django.db import models


class Booking(models.Model):
    class Meta:
        db_table = 'bookings'

    book_ref = models.CharField(verbose_name='номер брони', max_length=9)
    book_date = models.DateTimeField(verbose_name='дата бронирования', auto_now_add=True)
    total_amount = models.FloatField(verbose_name='Итоговая цена')

    def __str__(self):
        return self.book_ref