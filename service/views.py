from service.models import Booking
from django.db import models
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def book_ride(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        passengers = request.POST.get("passengers")
        pickup = request.POST.get("pickup")
        drop = request.POST.get("drop")
        date = request.POST.get("date")
        time = request.POST.get("time")
        booking = Booking(name=name, email=email, phone=phone, passengers=passengers, pickup=pickup, drop=drop, date=date, time=time)
        booking.save()
    return render(request, 'bookride.html')

def contact(request):
    return render(request, 'contact.html')

def bookings(request):
    history = Booking.objects.all().order_by('-date')
    context = {'history': history}
    return render(request, 'customer.html', context)
