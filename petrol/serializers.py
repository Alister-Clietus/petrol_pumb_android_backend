# serializers.py
from rest_framework import serializers
from .models import Dispenser, FuelTransaction

class DispenserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dispenser
        fields = ['dispenser_id', 'petrol_rate', 'diesel_rate', 'petrol_stock', 'diesel_stock','dispensing_mode']



class FuelTransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FuelTransaction
        fields = '__all__'