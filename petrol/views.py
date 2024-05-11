from django.http import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.
# views.py
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from authentication.models import User
from .models import Dispenser
from .serializers import DispenserSerializer, FuelTransactionSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@api_view(['POST'])
def create_or_update_dispenser_detail(request):
    try:
        dispenser_id = request.data.get('dispenser_id')
        if dispenser_id is not None:
            try:
                dispenser = Dispenser.objects.get(dispenser_id=dispenser_id)
                serializer = DispenserSerializer(dispenser, data=request.data)
            except Dispenser.DoesNotExist:
                serializer = DispenserSerializer(data=request.data)
        else:
            serializer = DispenserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'successfull'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def get_dispenser_detail(request, dispenser_id):
    try:
        dispenser = Dispenser.objects.get(dispenser_id=dispenser_id)
        serializer = DispenserSerializer(dispenser)
        return Response(serializer.data)
    except Dispenser.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['PUT'])
def enable_dispenser_mode(request, dispenser_id):
    try:
        dispenser = Dispenser.objects.get(dispenser_id=dispenser_id)
        dispenser.dispensing_mode = True
        dispenser.save()
        return Response({'message': 'Dispenser mode enabled successfully'}, status=status.HTTP_200_OK)
    except Dispenser.DoesNotExist:
        return Response({'error': 'Dispenser not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['PUT'])
def disable_dispenser_mode(request, dispenser_id):
    try:
        dispenser = Dispenser.objects.get(dispenser_id=dispenser_id)
        dispenser.dispensing_mode = False
        dispenser.save()
        return Response({'message': 'Dispenser mode disabled successfully'}, status=status.HTTP_200_OK)
    except Dispenser.DoesNotExist:
        return Response({'error': 'Dispenser not found'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
# views.py
@api_view(['PUT'])
def update_rates(request):
    try:
        new_petrol_rate = request.data.get('petrol_rate')
        new_diesel_rate = request.data.get('diesel_rate')

        if new_petrol_rate is None and new_diesel_rate is None:
            return Response({'error': 'No update parameters provided'}, status=status.HTTP_400_BAD_REQUEST)

        if new_petrol_rate is not None:
            Dispenser.objects.update(petrol_rate=new_petrol_rate)

        if new_diesel_rate is not None:
            Dispenser.objects.update(diesel_rate=new_diesel_rate)

        return Response({'message': 'Successfully'}, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


def get_all_dispensers(request):
    # Query all instances of the Dispenser model
    dispensers = Dispenser.objects.all()
    
    # Serialize data into JSON format
    data = []
    for dispenser in dispensers:
        data.append({
            'dispenser_id': dispenser.dispenser_id,
            'petrol_rate': dispenser.petrol_rate,
            'diesel_rate': dispenser.diesel_rate,
            'petrol_stock': dispenser.petrol_stock,
            'diesel_stock': dispenser.diesel_stock,
            'dispensing_mode': dispenser.dispensing_mode,
        })
    
    # Return JSON response
    return JsonResponse(data, safe=False)

@api_view(['POST'])
def fuel_transaction_create(request):
    if request.method == 'POST':
        serializer = FuelTransactionSerializer(data=request.data)
        if serializer.is_valid():
            username=serializer.validated_data['username']
            dispenser_id = serializer.validated_data['dispenser_id']
            fuel_type = serializer.validated_data['fuel_type']
            liters = serializer.validated_data['litters']

            try:
                dispenser = Dispenser.objects.get(dispenser_id=dispenser_id)
            except Dispenser.DoesNotExist:
                return Response({'error': 'Dispenser not found'}, status=status.HTTP_404_NOT_FOUND)
            
            

            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
            

            if fuel_type == 'petrol':
                if dispenser.petrol_stock < liters:
                    return Response({'error': 'Insufficient petrol stock'}, status=status.HTTP_400_BAD_REQUEST)
                dispenser.petrol_stock -= liters
            elif fuel_type == 'diesel':
                if dispenser.diesel_stock < liters:
                    return Response({'error': 'Insufficient diesel stock'}, status=status.HTTP_400_BAD_REQUEST)
                dispenser.diesel_stock -= liters

            dispenser.save()
            serializer.save()
            print("Received Fuel Transaction:")
            print(serializer.data)
            return Response({'message': 'FuelPurchased'}, status=status.HTTP_201_CREATED)
        return Response({'error': 'Mainerror Occured'}, status=status.HTTP_400_BAD_REQUEST)