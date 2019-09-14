from django.contrib import admin
from django.urls import path
from taroudant_etabs.views import *
from djgeojson.views import GeoJSONLayerView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view,name='home'),
    path('home', home_view,name='home'),
    path(r'webmap', webmap_view,name='webmap'),
    path(r'data', GeoJSONLayerView.as_view(model= Etablissements, properties=('Nom','Cycle','Effectif_total','Nombre_Enseignant','Type','Superficie')),name='data'),

]
