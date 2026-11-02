from django.db import models
from django.contrib.auth.models import User

class Reservation(models.Model):
date = models.CharField(max_length=100)
time = models.CharField()
Nombre de personnes = models.CharField(max_length=100)
statut = models.CharField()


def_str_(self):
return self.date

```
utilisateur = models.ForeignKey(
    User,
    on_delete=models.CASCADE
)

date_reservation = models.DateTimeField(
    auto_now_add=True
)

nombre_places = models.PositiveIntegerField(default=1)

statut = models.CharField(
    max_length=20,
    choices=[
        ('EN_ATTENTE', 'En attente'),
        ('CONFIRMEE', 'Confirmée'),
        ('ANNULEE', 'Annulée'),
    ],
    default='EN_ATTENTE'
)

def confirmer(self):
    self.statut = 'CONFIRMEE'
    self.save()

def annuler(self):
    self.statut = 'ANNULEE'
    self.save()

def __str__(self):
    return f"Réservation {self.id} - {self.statut}"
```
