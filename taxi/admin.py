from django.contrib import admin
from .models import taxis

class TaxiAdmin(admin.ModelAdmin):
    fields = ["taxi_num",
              "rate",
              "avail",
              "driver_name",
              "driver_no"]


admin.site.register(taxis,TaxiAdmin)