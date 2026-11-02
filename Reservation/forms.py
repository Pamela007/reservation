from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

class Meta:
    model = Reservation

    fields = [
        'date_reservation',
        'nombre_places',
        'statut'
    ]

    widgets = {
        'date_reservation': forms.DateTimeInput(attrs={
            'class': 'input input-bordered w-full',
            'type': 'datetime-local'
        }),

        'nombre_places': forms.NumberInput(attrs={
            'class': 'input input-bordered w-full',
            'placeholder': 'Nombre de places',
            'min': '1'
        }),

        'statut': forms.Select(attrs={
            'class': 'select select-bordered w-full'
        })
    }

