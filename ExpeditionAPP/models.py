from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from EntrepriseAPP.models import Entreprise
# Create your models here.
class Expedition(models.Model):
    reference = models.CharField(max_length=200, unique=True, blank=True)
    ville_depart=models.CharField(max_length=200)
    ville_arrive=models.CharField(max_length=200)
    poids_kg = models.DecimalField(
        max_digits=4,
        decimal_places=3,
        validators=[MinValueValidator(0)]
)
    date_souhaitee=models.DateField()
    description=models.TextField()
    statut=models.CharField(max_length=50,choices = [('a','annulle'),('e','encours'),('p','publiee')],default='e')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    entreprise = models.ForeignKey(Entreprise, on_delete=models.CASCADE, related_name='expeditions')

    @classmethod
    def _generate_reference(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"EXP_{annee}"
        dernier = (
            cls.objects.filter(reference__startswith=prefixe)
            .order_by('-reference')
            .first()
        )
        compteur = int(dernier.reference[-5:]) + 1 if dernier else 1
        if compteur > 99999:
            raise ValidationError("le compteur a depasse la limite maximale")
        return f"{prefixe}{compteur:05d}"

    def save(self, *args, **kwargs):
        if not self.reference:
            self.reference = self._generate_reference()
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self):
        super().clean()
        if self.entreprise_id and self.entreprise.type_entreprise != 'c':
            raise ValidationError({
                'entreprise': 'Une expedition ne peut etre creee que par un chargeur'})
    

