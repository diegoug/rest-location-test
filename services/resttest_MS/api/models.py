from django.db import models
from django.utils import timezone


class Driver(models.Model):
    name = models.CharField(
        'name', max_length=30)
    services = models.ManyToManyField('api.Service')

class Service(models.Model):
    workshop = models.ForeignKey(
        'api.Workshop', on_delete=models.PROTECT)
    date = models.DateTimeField(
        'date', default=timezone.now)
    latitude = models.DecimalField(
        max_digits=15, decimal_places=11)
    longitude = models.DecimalField(
        max_digits=15, decimal_places=11)

class Workshop(models.Model):
    workshop_id = models.CharField(max_length=30)
    name = models.CharField(
        'name', max_length=30)
    latitude = models.DecimalField(
        max_digits=15, decimal_places=11)
    longitude = models.DecimalField(
        max_digits=15, decimal_places=11)
    address = models.CharField(max_length=100)
