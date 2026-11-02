from django.contrib import admin
from django.urls import path 
from .import views 

urlpatterns = [
    path("", views.liste_Reservations , name="liste_Reservations" ),
    path("ajouter/", views.ajouter_Reservations , name="liste_Reservations" ),
    path("modifier/<int:id>/", views.modifier_Reservations , name="liste_Reservations" ),
    path("supprimer", views.supprimer_Reservations , name="supprimer_Reservations" ),
]