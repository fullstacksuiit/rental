
from django.contrib import admin
from django.urls import path
from service.views import book_ride, bookings, contact, index, about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="index"),
    path('about', about, name="about"),
    path('book', book_ride, name="book"),
    path('contact', contact, name="contact" ),
    path('bookings', bookings, name="bookings"),
]
