from .models import taxis,book,finishride
from django.forms import ModelForm

class Taxiform(ModelForm):
    class Meta:
        model=taxis
        fields=['taxi_num','rate','avail','driver_name','driver_no']

class Booktaxi(ModelForm):
    class Meta:
        model=book
        fields=['randomID','taxi_num']

class finishtaxi(ModelForm):
    class Meta:
        model=finishride
        fields = ['taxi_num', 'distance']
