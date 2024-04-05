from django.db import models


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    societe = models.CharField(max_length=100)
    adresse = models.CharField(max_length=200)
    telFixe = models.CharField(max_length=20)
    telMobile = models.CharField(max_length=20)
    besoin = models.TextField()

    def __str__(self):
        return self.nom
