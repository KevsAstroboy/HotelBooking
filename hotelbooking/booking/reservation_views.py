from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import datetime

from .models import *

@login_required(login_url='login')
class ReservationView(View):

    template_index = 'reservation.html'
    date_format = "%m/%d/%Y"

    def get(self, request):

        if not request.user.is_authenticated:
            return redirect('login')

        room_id = request.GET.get('room')
        hotels = Hotel.objects.all()
        rooms = Chambre.objects.all()
        context = {
            'hotels': hotels,
            'rooms': rooms,
            'room_id': room_id
        }
        return render(request, self.template_index, context)

    def post(self, request):
        if request.method == 'POST':
            user_id = request.POST.get('user')
            chambre_id = request.POST.get('chambre')
            date_reservation = request.POST.get('date-reservation')
            date_fin = request.POST.get('date-fin')
            hotel_id = request.POST.get('hotel')

            if not all([user_id, chambre_id, date_reservation, date_fin, hotel_id]):
                messages.error(request, 'Veuillez bien renseigner les différents champs')

            else:
                user = User.objects.get(id=user_id)
                chambre = Chambre.objects.get(id=chambre_id)
                hotel = Hotel.objects.get(id=hotel_id)

                reservation_date = datetime.strptime(date_reservation, self.date_format).date()
                end_date = datetime.strptime(date_fin, self.date_format).date()

                if reservation_date < datetime.today().date():
                    messages.error(request, 'La date de réservation est déjà passée')

                elif reservation_date >= end_date:
                    messages.error(request, 'La date de fin doit être après la date de réservation')

                elif chambre.nombre_disponible < 1:
                    messages.error(request, 'La chambre sélectionnée n\'est pas disponible')

                else:
                    chambre.nombre_disponible -= 1
                    chambre.save()

                    new_reservation = Reservation.objects.create(
                        id_hotel=hotel,
                        id_chambre=chambre,
                        date_reservation=reservation_date,
                        date_fin=end_date,
                        user=user
                    )
                    new_reservation.save()

                    messages.success(request, 'Réservation effectuée avec succès')

        return redirect('reservation')
