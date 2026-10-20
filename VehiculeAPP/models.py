from django.db import models
from EntrepriseAPP.models import Entreprise
from django.core.validators import MinValueValidator

# Create your models here.
class Vehicule(models.Model):
    immatriculation=models.CharField(max_length=200,unique=True)
    type_vehicule=models.CharField(max_length=50,choices = [('A','A'),('B','B')],default='B')
    Disponible=models.BooleanField(default=False)
    capacite_kg = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey(Entreprise,on_delete=models.CASCADE)