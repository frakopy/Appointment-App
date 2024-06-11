from django.db import models

class Barber(models.Model):
    name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    phone = models.PositiveIntegerField()
    email = models.CharField(max_length=250)

    class Meta:
        verbose_name = 'Barber'
        verbose_name_plural = 'Barbers'

    def __str__(self):
        return self.name

