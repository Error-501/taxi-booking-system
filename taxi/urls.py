from django.urls import path
from . import views

app_name= "taxi"

urlpatterns = [
    path("", views.homepage, name="home"),
    path("addtaxi/", views.addtaxi, name="addtaxi"),
    path("booktaxi/", views.booktaxi, name="booktaxi"),
    path("finish/", views.finishride, name="finishride"),
]