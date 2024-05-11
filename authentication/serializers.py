# serializers.py
from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'wallet_amount', 'petrol_purchased', 'diesel_purchased', 'current_petrol_rate', 'current_diesel_rate']

class UserWalletUpdateSerializer(serializers.Serializer):
    email = serializers.EmailField()
    wallet_amount = serializers.DecimalField(max_digits=10, decimal_places=2)
