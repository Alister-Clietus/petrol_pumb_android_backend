from django.db import models

class User(models.Model):
    email = models.EmailField(primary_key=True)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    wallet_amount = models.DecimalField(max_digits=10, decimal_places=2)
    petrol_purchased = models.DecimalField(max_digits=10, decimal_places=2)
    diesel_purchased = models.DecimalField(max_digits=10, decimal_places=2)
    current_petrol_rate = models.DecimalField(max_digits=6, decimal_places=2)
    current_diesel_rate = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        # Optional: Define unique constraint for the email field
        unique_together = ('email',)
