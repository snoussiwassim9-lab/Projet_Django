from django.contrib import admin
from .models import Vehicule


@admin.register(Vehicule)
class VehiculeAdmin(admin.ModelAdmin):
    list_display = ('immatriculation', 'type_vehicule', 'capacite_kg', 'Disponible', 'entreprise', 'created_at')
    list_filter = ('type_vehicule', 'Disponible')
    search_fields = ('immatriculation', 'entreprise__rasion_social')
    list_editable = ('Disponible',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_per_page = 25

    autocomplete_fields = ('entreprise',)
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        ('Identification', {'fields': ('immatriculation', 'type_vehicule', 'entreprise')}),
        ('Caracteristiques', {'fields': ('capacite_kg', 'Disponible')}),
        ('Suivi', {'fields': ('created_at', 'updated_at')}),
    )
