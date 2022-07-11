from django.shortcuts import render, redirect
from .models import Chofer, Pasajero
from .forms import ChoferForm, PasajeroForm 
# Create your views here.
def chofer(request):
    chofer = Chofer.objects.all()

    datos = {
        'chofer': chofer
    }
    return render(request, 'chofer.html', datos)

def index(request):

    return render(request, 'index.html')


def final(request):
    chofer = Chofer.objects.all()
    datos = {
        'chofer': chofer
    }
    return render(request, 'final.html', datos)



def form_del_chofer(request, id):
    chofer = Chofer.objects.get(rut=id)
    chofer.delete()
    return redirect ('chofer')

def form_pasajero(request):
    if request.method=='POST': 
        pasajero_form = PasajeroForm(request.POST)
        if pasajero_form.is_valid():
            pasajero_form.save()
            return redirect('chofer')
    else:
        pasajero_form= PasajeroForm()
    return render(request, 'form_pasajero.html', {'pasajero_form': pasajero_form})

def form_del_pasajero(request, id):
    pasajero = Pasajero.objects.get(rut=id)
    pasajero.delete()
    return redirect ('final')