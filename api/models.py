from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class MyVehicle(models.Model):
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)
    # trackerId = models.CharField(max_length=10)
    latitude  = models.FloatField(blank=0.00)
    longitude = models.FloatField(blank=0.00)
    isFixed = models.FloatField(blank=0.00)
    timeStamp = models.DateTimeField(auto_now_add=True)
    speed = models.FloatField(blank=0.00)
    bearing = models.FloatField(blank=0.00)
    altitude = models.FloatField(blank=0.00)
    accuracy = models.FloatField(blank=0.00)
    battery_level = models.FloatField(blank=0.00)
    

class VehicleSwitch(models.Model):
    immobilisation_switch_state = models.BooleanField(blank=False)