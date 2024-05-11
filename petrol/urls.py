from django.contrib import admin
from django.urls import path

from petrol.models import get_petrol_diesel_rate
from . import views

urlpatterns = [
        path('dispenser/<int:dispenser_id>/', views.get_dispenser_detail, name='get_dispenser_detail'),
        path('dispenser/', views.create_or_update_dispenser_detail, name='create_or_update_dispenser_detail'),
        path('dispenser/<int:dispenser_id>/enable/', views.enable_dispenser_mode, name='enable_dispenser_mode'),
        path('dispenser/<int:dispenser_id>/disable/', views.disable_dispenser_mode, name='disable_dispenser_mode'),
        path('update-rates/', views.update_rates, name='update_rates'),
        path('rate/', get_petrol_diesel_rate, name='petrol_diesel_rate'),
        path('dispensers/', views.get_all_dispensers, name='all_dispensers'),
        path('purchase-fuel/', views.fuel_transaction_create, name='fuel_transaction_create'),


]