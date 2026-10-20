from django.db import models
from VehiculeAPP.models import Vehicule
from ExpeditionAPP.models import Expedition
from EntrepriseAPP.models import Entreprise


# Create your models here.
class Offre(models.Model) : 
    prix=models.DecimalField(max_digits=10, decimal_places=2)
    delai_jours=models.PositiveIntegerField()
    statut=models.CharField(max_length=50,choices=[('a','accepte'),('r','refusee')],default='a')
    date_proposition=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    expedition=models.ForeignKey(Expedition,on_delete=models.CASCADE)
    transporteur=models.ForeignKey(Entreprise,on_delete=models.CASCADE)
    vehicule=models.ForeignKey(Vehicule,on_delete=models.CASCADE)
    



