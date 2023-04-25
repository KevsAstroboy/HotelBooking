from django.urls import path
from .user_views import *
from .chambre_views import *
from .reservation_views import * 


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('chambres/', ChambreView.as_view(), name='chambres'),
    path('reservation/', ReservationView.as_view(), name= 'reservation')
]