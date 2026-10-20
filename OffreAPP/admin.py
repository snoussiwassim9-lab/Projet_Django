from django.contrib import admin
from django.utils.html import format_html
from .models import Offre


class PrixFilter(admin.SimpleListFilter):
    title = 'prix'
    parameter_name = 'prix_max'

    def lookups(self, request, model_admin):
        return [
            ('100', 'Inferieur a 100'),
            ('1000', 'Inferieur a 1000'),
            ('2000', 'Inferieur a 2000'),
        ]

    def queryset(self, request, queryset):
        if self.value() in ('100', '1000', '2000'):
            return queryset.filter(prix__lt=self.value())
        return queryset


@admin.register(Offre)
class OffreAdmin(admin.ModelAdmin):
    list_display = ('expedition', 'transporteur', 'vehicule', 'prix', 'delai_jours', 'statut', 'date_proposition')
    list_filter = ('statut', PrixFilter)
    search_fields = ('expedition__reference', 'transporteur__rasion_social')
    list_editable = ('statut',)
    ordering = ('-created_at',)
    date_hierarchy = 'date_proposition'
    list_per_page = 25

    autocomplete_fields = ('expedition', 'transporteur', 'vehicule')
    readonly_fields = ('statut_colore', 'date_proposition', 'created_at', 'updated_at')
    fieldsets = (
        ("Details de l'offre", {'fields': ('expedition', 'transporteur', 'vehicule')}),
        ('Conditions', {'fields': ('prix', 'delai_jours')}),
        ('Suivi', {'fields': ('statut_colore', 'statut', 'date_proposition', 'created_at', 'updated_at')}),
    )

    @admin.display(description='Statut')
    def statut_colore(self, obj):
        couleurs = {
            'a': '#5CB85C',
            'r': '#D9534F',
        }
        return format_html(
            '<span style="color:white;background:{};padding:3px 8px;border-radius:4px;">{}</span>',
            couleurs.get(obj.statut, '#999'), obj.get_statut_display(),
        )
