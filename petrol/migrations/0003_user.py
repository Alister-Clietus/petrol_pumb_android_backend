# Generated by Django 4.0 on 2024-05-08 03:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petrol', '0002_dispenser_dispensing_mode'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('wallet_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('petrol_purchased', models.DecimalField(decimal_places=2, max_digits=10)),
                ('diesel_purchased', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_petrol_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('current_diesel_rate', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'unique_together': {('email',)},
            },
        ),
    ]
