from django.urls import path
from .views import index, form_del_chofer, chofer, form_pasajero, form_del_pasajero, final

urlpatterns = [
    path('', index, name="index"),
    path('chofer/', chofer, name="chofer"),
    path('final/', final, name="final"),
    path('form_del_chofer/<id>', form_del_chofer, name="form_del_chofer"),
    path('form_del_pasajero/<id>', form_del_pasajero, name="form_del_chofer"),
    path('form_pasajero/', form_pasajero, name="form_pasajero"),
    ] 