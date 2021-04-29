from django.db import models
from django.forms import ModelForm


class taxis(models.Model):
    CHOICES = [
        ('YES','yes'),
        ('NO','no'),
    ]

    taxi_num = models.CharField(max_length=10)
    rate = models.FloatField()
    avail = models.CharField(max_length=3, choices=CHOICES)
    driver_name = models.CharField(max_length=20)
    driver_no = models.IntegerField()

    def __str__(self):
        return self.taxi_num

class book(models.Model):

    taxi_num = models.CharField(max_length=10)
    randomID =models.IntegerField()

    def __str__(self):
        return self.taxi_num

class finishride(models.Model):

    taxi_num = models.CharField(max_length=10)
    distance =models.IntegerField()

    def __str__(self):
        return self.taxi_num

