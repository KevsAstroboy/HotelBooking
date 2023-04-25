import datetime
from django.db import models
from django.contrib.auth.models import User


class Hotel(models.Model):
    nom_hotel = models.CharField(max_length=50)
    logo_hotel = models.FileField(upload_to='tools')

    def __str__(self):
        return self.nom_hotel


class Chambre(models.Model):
    nom_chambre = models.CharField(max_length=100)
    id_hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    numero_chambre = models.BigIntegerField()
    nombre_disponible = models.BigIntegerField(default=10)
    prix_chambre = models.BigIntegerField()

    def __str__(self):
        return self.nom_chambre


class HotelPhoto(models.Model):
    id_hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='tools')


class ChambrePhoto(models.Model):
    id_chambre = models.ForeignKey(Chambre, on_delete=models.SET_NULL, null=True)
    photo = models.FileField(upload_to='tools')


class Reservation(models.Model):
    id_hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True)
    id_chambre = models.ForeignKey(Chambre, on_delete=models.SET_NULL, null=True)
    date_reservation = models.DateField()
    date_fin = models.DateField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user
