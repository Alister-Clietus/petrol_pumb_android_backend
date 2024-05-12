# views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer, UserWalletUpdateSerializer
from django.contrib.auth.hashers import check_password
from rest_framework.views import APIView


@api_view(['POST'])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    print(serializer)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Userfound'}, status=status.HTTP_201_CREATED)
    print(serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_user_details(request, username):
    try:
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    

@api_view(['POST'])
def authenticate_user(request):
    try:
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.get(username=username)
        if(password==user.password):
            if username == 'archa' or username == 'admin':
                return Response({'message': 'adminsuccessful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'successful'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'failed'}, status=status.HTTP_401_UNAUTHORIZED)
    except User.DoesNotExist:
        return Response({'message': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
    
class UserWalletUpdate(APIView):
    def put(self, request, *args, **kwargs):
        serializer = UserWalletUpdateSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            wallet_amount = serializer.validated_data['wallet_amount']
            
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
            
            user.wallet_amount = wallet_amount
            user.save()
            
            return Response({"message": "Wallet amount updated successfully"}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)