from django.contrib import admin
from django.utils import timezone
from django.utils.html import format_html
from .models import Expedition


class EnRetardFilter(admin.SimpleListFilter):
    title = 'en retard'
    parameter_name = 'en_retard'

    def lookups(self, request, model_admin):
        return [('oui', 'Oui'), ('non', 'Non')]

    def queryset(self, request, queryset):
        if self.value() == 'oui':
            return queryset.filter(statut='e', date_souhaitee__lt=timezone.now().date())
        if self.value() == 'non':
            return queryset.exclude(statut='e', date_souhaitee__lt=timezone.now().date())
        return queryset


@admin.register(Expedition)
class ExpeditionAdmin(admin.ModelAdmin):
    list_display = ('reference', 'entreprise', 'ville_depart', 'ville_arrive', 'statut', 'date_souhaitee')
    list_filter = ('statut', 'ville_depart', EnRetardFilter)
    search_fields = ('reference', 'entreprise__rasion_social')
    list_editable = ('statut',)
    ordering = ('-created_at',)
    date_hierarchy = 'date_souhaitee'
    list_per_page = 25

    autocomplete_fields = ('entreprise',)
    readonly_fields = ('reference', 'statut_colore', 'created_at', 'updated_at')
    fieldsets = (
        ("Details de l'expedition", {'fields': ('reference', 'entreprise', 'ville_depart', 'ville_arrive')}),
        ('Caracteristiques', {'fields': ('poids_kg', 'date_souhaitee', 'description')}),
        ('Suivi', {'fields': ('statut_colore', 'statut', 'created_at', 'updated_at')}),
    )

    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'a': '#D9534F',
            'e': '#5CB85C',
        }
        return format_html(
            '<span style="color:white;background:{};padding:3px 8px;border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999'), obj.get_statut_display(),
        )
