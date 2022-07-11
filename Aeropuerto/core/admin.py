from django.contrib import admin
from .models import Categoria, Chofer, Pasajero

# Register your models here.

admin.site.register(Categoria)
admin.site.register(Chofer)
admin.site.register(Pasajero)