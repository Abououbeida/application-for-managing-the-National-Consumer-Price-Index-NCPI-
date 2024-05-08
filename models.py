
# Create your models here.
# ansade_app/models.py

from django.db import models

class FamilleProduit(models.Model):
    nom = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nom

class Produit(models.Model):
    nom = models.CharField(max_length=255)
    description = models.TextField()
    famille = models.ForeignKey(FamilleProduit, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom
