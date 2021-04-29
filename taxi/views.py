from django.shortcuts import render,redirect
from .models import taxis
from .forms import Taxiform,Booktaxi,finishtaxi
from django.contrib import messages
import random

# Create your views here.
def homepage(request):
    return render(request=request,
                  template_name="taxis/home.html",context={"objs":taxis.objects.all().filter(avail='YES'),"book":taxis.objects.all().filter(avail='NO')})

def addtaxi(request):
    if request.method == 'POST':
        form = Taxiform(request.POST)
        if form.is_valid():
            form.save()
            taxi_num = form.cleaned_data.get('taxi_num')
            messages.info(request, f"New taxi with no {taxi_num} added")
            return redirect("taxi:home")
        else:
            return render(request=request,
                          template_name="taxis/addtaxi.html",
                          context={"form": form})
    form = Taxiform()
    return render(request=request, template_name="taxis/addtaxi.html", context={"form": form})

def booktaxi(request):
    randomID=random.randint(30000000, 90000000)
    if request.method == 'POST':
        form = Booktaxi(request.POST)
        if form.is_valid():
            form.save()
            taxi_num = form.cleaned_data.get('taxi_num')
            try:
                check=taxis.objects.all().filter(taxi_num=taxi_num)
                c = check.values_list('avail', flat=True)[::1][0]
            except:
                messages.info(request, "Check Taxi Number")
                form = Booktaxi(initial={'randomID': randomID})
                return render(request=request, template_name="taxis/booktaxi.html", context={"form": form})
            print(c)
            if c == 'YES':
                taxis.objects.all().filter(taxi_num=taxi_num).update(avail='NO')
                messages.info(request, f"Taxi no {taxi_num} booked")
                return redirect("taxi:home")
            else:
                messages.info(request, f"Taxi not available")
                form = Booktaxi(initial={'randomID': randomID})
                return render(request=request, template_name="taxis/booktaxi.html", context={"form": form})
        else:
            messages.error(request, "Pls input crct data")
            return render(request=request,
                          template_name="taxis/booktaxi.html",
                          context={"form": form})
    form = Booktaxi(initial={'randomID': randomID})
    return render(request=request, template_name="taxis/booktaxi.html", context={"form": form})

def finishride(request):
    if request.method == 'POST':
        form = finishtaxi(request.POST)
        if form.is_valid():
            form.save()
            taxi_num = form.cleaned_data.get('taxi_num')
            rate = form.cleaned_data.get('distance')
            try:
                check=taxis.objects.all().filter(taxi_num=taxi_num)
                c = check.values_list('avail', flat=True)[::1][0]
            except:
                messages.info(request, "Check Taxi Number")
                return render(request=request, template_name="taxis/finish.html", context={"form": form})
            print(c)
            if c == 'NO':
                taxis.objects.all().filter(taxi_num=taxi_num).update(avail='YES')
                r = rate * check.values_list('rate', flat=True)[::1][0]
                messages.info(request, f"Taxi no {taxi_num} ride ended ")
                messages.info(request, f"Ride Fair is {r} ")
                return redirect("taxi:home")
            else:
                return render(request=request, template_name="taxis/finish.html", context={"form": form})
        else:
            messages.error(request, "Pls input crct data")
            return render(request=request,
                          template_name="taxis/finish.html",
                          context={"form": form})
    form = finishtaxi()
    return render(request=request, template_name="taxis/finish.html", context={"form": form})