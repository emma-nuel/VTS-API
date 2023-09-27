from rest_framework import serializers
from api.models import MyVehicle, VehicleSwitch

class MyVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyVehicle
        fields = '__all__'

class ImmobilisationSwitchSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleSwitch
        fields = '__all__'
    
    
