from django.contrib import admin
from .models import Etablissements
from leaflet.admin import LeafletGeoAdmin
# Register your models here.

class EtablissementsAdmin(LeafletGeoAdmin):
    list_display=('Nom','Latitude','Longitude','Cycle','Type')
    readonly_fields = ('Latitude','Longitude')
    list_filter= ('Effectif_total','Cycle')

admin.site.register(Etablissements,EtablissementsAdmin)
