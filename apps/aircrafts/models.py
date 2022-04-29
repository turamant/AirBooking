from django.db import models

class Aircraft(models.Model):
    aircraft_code = models.CharField(unique=True, max_length=3)
    model = models.JSONField()
    range = models.PositiveIntegerField()

    def __str__(self):
        return self.aircraft_code

