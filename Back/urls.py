from django.urls import path
from . import views

urlpatterns = [
    path('contact/', views.formulaire_contact, name='formulaire_contact'),
]
