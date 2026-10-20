from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from django.core.exceptions import ValidationError
from django.utils import timezone

# Create your models here.
def validate_email(value): 
    if not value : 
        raise ValidationError("L'adresse doit s etre en forme")
    if not value.endswith('gmail.com') :
        raise ValidationError('l adress doit s etre en forme ')
matricule_fiscale_validator=RegexValidator(regex=r'^\d{7}[/ -]?[A-Za-z][/ -]?[ABDNPEabdnpe][/ -]?[MPCNEmpcne][/ -]?\d{3}$', message="Format errone")
user_id_validator=RegexValidator(regex=r'^\d{2}user\d{2}$', message="Format doit etre AAuserNN")

class Utilisateur (AbstractUser):
    user_id=models.CharField(primary_key=True,max_length=8,validators=[user_id_validator])
    email = models.EmailField(unique=True , validators=[validate_email])
    telephone =models.CharField(max_length=15,blank=True,null=True)
    role=models.CharField(max_length=20,choices=[('admin','Admin'),('c','Chargeur'),('t','Transporteur')],default='c')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    @classmethod
    def _generate_user_id(cls):
        annee = timezone.now().strftime('%y')
        prefixe = f"{annee}user"
        dernier = (
            cls.objects.filter(user_id__startswith=prefixe)
            .order_by('-user_id')
            .first()
        )
        compteur = int(dernier.user_id[-2:]) + 1 if dernier else 0
        if compteur > 99:
            raise ValidationError("le compteur a depasse la limite maximale")
        return f"{prefixe}{compteur:02d}"

    def save(self, *args, **kwargs):
        if not self.user_id:
            self.user_id = self._generate_user_id()
        self.full_clean()
        super().save(*args, **kwargs)
    

class Entreprise(models.Model): 
    rasion_social = models.CharField(max_length=200 , blank=False , null = False)
    matricule_fiscal=models.CharField(max_length=17,unique = True,validators=[matricule_fiscale_validator])
    adresse = models.TextField(validators=[MinLengthValidator(20,"L adresse doit ne passe pas 20 char"),MaxLengthValidator(400,"The message should not pass 400 Chars")])
    type_entreprise=models.CharField(max_length=100,choices = [('c','Chargeur'),('t','Transporteur')],default='c')
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    gerant = models.OneToOneField(Utilisateur,on_delete=models.CASCADE , related_name='entreprise')