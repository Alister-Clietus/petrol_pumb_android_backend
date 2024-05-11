from django.db import models
from django.http import JsonResponse

class Dispenser(models.Model):
    dispenser_id = models.IntegerField(primary_key=True)
    petrol_rate = models.DecimalField(max_digits=10, decimal_places=2)
    diesel_rate = models.DecimalField(max_digits=10, decimal_places=2)
    petrol_stock = models.IntegerField()
    diesel_stock = models.IntegerField()
    dispensing_mode = models.BooleanField(default=False)



class FuelTransaction(models.Model):
    username = models.CharField(max_length=100)
    dispenser_id = models.CharField(max_length=100)
    litters = models.DecimalField(max_digits=10, decimal_places=2)
    fuel_type = models.CharField(max_length=100)
    
def get_petrol_diesel_rate(request):
    # Assuming you want to fetch data from any one dispenser
    # You can change the logic as per your requirement
    
    # Get data from any one dispenser (you can change this logic)
    dispenser = Dispenser.objects.first()
    
    # Check if dispenser exists
    if dispenser:
        # Serialize data into JSON format
        data = {
            'petrol_rate': dispenser.petrol_rate,
            'diesel_rate': dispenser.diesel_rate,
        }
        # Return JSON response
        return JsonResponse(data)
    else:
        # If no dispenser exists, return an error message
        return JsonResponse({'error': 'No dispenser found'}, status=404)
    