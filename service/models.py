from django.db import models

class Service(models.Model):
    name = models.CharField(max_length=250)
    price = models.FloatField()
    description = models.TextField()

    class Meta:
        verbose_name = ("Service")
        verbose_name_plural = ("Services")

    def __str__(self):
        return self.name
