from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Utilisateur, Entreprise
from VehiculeAPP.models import Vehicule


class UtilisateurCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ('username', 'email', 'role', 'telephone')


class UtilisateurChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = Utilisateur
        fields = '__all__'


@admin.register(Utilisateur)
class UtilisateurAdmin(UserAdmin):
    add_form = UtilisateurCreationForm
    form = UtilisateurChangeForm
    model = Utilisateur

    list_display = ('user_id', 'username', 'email', 'role', 'telephone', 'created_at')
    list_filter = ('role',)
    search_fields = ('user_id', 'username', 'email', 'telephone')
    list_editable = ('role',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25

    readonly_fields = ('user_id', 'created_at', 'updated_at', 'last_login', 'date_joined')
    fieldsets = (
        (None, {'fields': ('user_id', 'username', 'password')}),
        ('Informations personnelles', {'fields': ('first_name', 'last_name', 'email', 'telephone')}),
        ('Role et permissions', {'fields': ('role', 'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Dates importantes', {'fields': ('last_login', 'date_joined', 'created_at', 'updated_at')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'telephone', 'role', 'password1', 'password2'),
        }),
    )


class VehiculeInline(admin.TabularInline):
    model = Vehicule
    extra = 2
    fields = ('immatriculation', 'type_vehicule', 'capacite_kg', 'Disponible')
    show_change_link = True


@admin.register(Entreprise)
class EntrepriseAdmin(admin.ModelAdmin):
    list_display = ('rasion_social', 'matricule_fiscal', 'type_entreprise', 'gerant', 'created_at')
    list_filter = ('type_entreprise',)
    search_fields = ('rasion_social', 'matricule_fiscal')
    list_editable = ('type_entreprise',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25

    autocomplete_fields = ('gerant',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Informations generales', {'fields': ('rasion_social', 'matricule_fiscal', 'type_entreprise')}),
        ('Contact', {'fields': ('adresse', 'gerant')}),
        ('Suivi', {'fields': ('created_at', 'updated_at')}),
    )
    inlines = [VehiculeInline]
