from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Hotel)
admin.site.register(Chambre)
admin.site.register(HotelPhoto)
admin.site.register(ChambrePhoto)
admin.site.register(Reservation)