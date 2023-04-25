from django.shortcuts import render, redirect
from django.views import View
from django.shortcuts import render


from .serializer import UserSerializer
from django.contrib import messages
from django.contrib.auth import authenticate , login , logout
from .models import *


class HomeView(View):

    template_index = 'index.html'


    def get(self, request):
        if request.method == 'GET':
            value = request.GET.get('submit')
            if value == 'Logout':
                logout(request)
                return redirect('home')
        hotels = Hotel.objects.all()
        rooms = Chambre.objects.all()
        rooms_photos = ChambrePhoto.objects.all()
        best_rooms = Chambre.objects.filter(nom_chambre__in=['Chambre Coucoué Lodge', 'Suite Lodge by Coucoué'])
        best_room_ids = [room.id for room in best_rooms]
        best_room_photos = ChambrePhoto.objects.filter(id__in=best_room_ids)
        photos_hotel = HotelPhoto.objects.all()
        context = {'hotels': hotels, 
                    'photos': photos_hotel,
                    'best_rooms': best_rooms,
                    'best_room_photos': best_room_photos,
                    'rooms': rooms,
                    'rooms_photos': rooms_photos
                }
        
        return render(request, self.template_index,context)


    


class RegisterView(View):
    template_index = 'register.html'
    
    def get(self, request):
        hotels = Hotel.objects.all()
        photos_hotel = HotelPhoto.objects.all()
        serialize = UserSerializer()
        context = {
            'hotels': hotels,
            'photos': photos_hotel,
            'form': serialize,
        }
        return render(request, self.template_index, context)

    def post(self, request):

            if request.method == 'POST':
                user = User.objects.filter(username = request.POST.get('username'))
                if user.exists():
                        messages.warning(request,"Username is already exists")
                serialize = UserSerializer(request.POST)
                if serialize.is_valid():
                    serialize.save()
                    messages.success(request, 'Compte a été crée avec succès')
                    return redirect('register')
            messages.error(request, 'Veuillez bien renseigner tous les champs requis')
            context = {'form': serialize}
            return render(request, self.template_index, context)


class LoginView(View):
    template_index = 'login.html'
    
    def get(self, request):
        hotels = Hotel.objects.all()
        photos_hotel = HotelPhoto.objects.all()
        serialize = UserSerializer()
        context = {
            'hotels': hotels,
            'photos': photos_hotel,
            'form': serialize,
        }
        return render(request, self.template_index, context)

    def post(self, request):
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')
            context = {}
        return render(request, self.template_index, context)

