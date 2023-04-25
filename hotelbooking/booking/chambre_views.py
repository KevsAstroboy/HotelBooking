from django.views import View
from django.shortcuts import render

from .models import Chambre, ChambrePhoto, Hotel


class ChambreView(View):
    template_index = 'rooms.html'

    def get(self, request):
        rooms = Chambre.objects.all()
        rooms_photos = ChambrePhoto.objects.all()
        hotels = Hotel.objects.all()
        context = {
            'rooms': rooms,
            'rooms_photos': rooms_photos,
            'hotels': hotels
        }
        return render(request, self.template_index, context)
