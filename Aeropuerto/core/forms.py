from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Chofer, Pasajero


class ChoferForm(forms.ModelForm):

    class Meta: 
        model= Chofer
        fields = ['nombre', 'rut', 'numero', 'patente', 'estacionamiento', 'categoria']
        labels ={
            'nombre': 'Nombre', 
            'rut': 'rut', 
            'numero': 'Numero',
            'patente': 'Patente',
            'estacionamiento': 'Estacionamiento',
            'categoria': 'Categoría',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre' 
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ),
            'numero': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Numero', 
                    'id': 'numero'
                }
            ), 
            'patente': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Patente', 
                    'id': 'patente'
                }
            ),
            'estacionamiento': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Estacionamiento', 
                    'id': 'estacionamiento'
                }
            ),                       
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class PasajeroForm(forms.ModelForm):

    class Meta: 
        model= Pasajero
        fields = ['nombre', 'rut', 'direccion', 'hora', 'categoria']
        labels ={
            'nombre': 'Nombre', 
            'rut': 'rut', 
            'direccion': 'Direccion',
            'hora': 'Hora',
            'categoria': 'Categoría',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre', 
                    'id': 'nombre' 
                }
            ), 
            'rut': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Rut', 
                    'id': 'rut'
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Direccion', 
                    'id': 'direccion'
                }
            ), 
            'hora': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese hora', 
                    'id': 'patente'
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }