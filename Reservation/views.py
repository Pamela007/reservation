from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm


def liste_Reservations(request):
Reservations = Reservation.objects.all()
return render(request , "Reservation/list.html", {"Reservations" : Reservations})


def ajouter_Reservation(request):
from = ReservationForm(request.POST or None)
if from.is_valid() :
from.save()
return redirect('liste_Reservations')
return render(request , 'Reservation/formulaire.html', {"form" : form})



   
 