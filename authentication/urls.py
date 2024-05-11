from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_user, name='create_user'),
    path('login/', views.authenticate_user, name='authenticate_user'),
    path('user/<str:username>/', views.get_user_details, name='get_user_details'),
    path('update-wallet/', views.UserWalletUpdate.as_view(), name='update_wallet'),

]