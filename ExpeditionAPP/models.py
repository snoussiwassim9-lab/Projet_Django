from django.db import models

# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(max_length=200, unique=True, blank=True)    ville_depart=models.CharField(max_length=200)
    ville_arrive=models.CharField(max_length=200)
    poids_kg=models.DecimalField(max_digits=4, decimal_places=3)
    date_souhaitee=models.DateField()
    description=models.TextField()
    statut=models.CharField(max_length=50,choices = [('a','annulle'),('e','encours')],default='e')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    



