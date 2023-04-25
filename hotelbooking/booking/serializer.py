from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from .models import *

class UserSerializer(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ReservationSerializer(ModelForm):
    class Meta:
        model = Reservation
        fields = ['id_hotel', 'id_chambre', 'date_reservation', 'date_fin', 'user']