from django.db import models

# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=50)
    email =  models.CharField(max_length=50, blank=True, null=True)
    phone = models.PositiveBigIntegerField()
    passengers = models.SmallIntegerField()
    pickup = models.CharField(max_length=100)
    drop = models.CharField(max_length=100, blank=True, null=True)
    date = models.DateField()
    time =  models.TimeField()
    ctype = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
         return self.name

