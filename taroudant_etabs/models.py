from django.db import models
from django.contrib.gis.db import models
from django.db.models import Manager as GeoManager
# Create your models here.
class Etablissements(models.Model):
    cycle_choices= (
    ( "Primaire","Primaire"),
    ("College","College"),
    ("Lycee","Lycee"),
    ("Université","Université")
)
    type_choices=(
    ("Public","Public"),
    ("Privé","Privé")

    )

    Nom= models.CharField(max_length=50)
    geom= models.PointField(srid=4326, blank= True,default=None)
    Cycle= models.CharField(max_length=200, choices= cycle_choices,null=False,default="Not selected" )
    Type= models.CharField(max_length=200, choices= type_choices,null=False,default="Not selected")
    Adress= models.CharField(max_length=200,default="Taroudant")
    Effectif_total= models.IntegerField(null=True,default=0)
    Nombre_Enseignant= models.IntegerField(null=True,default=0)
    Superficie= models.IntegerField(null=True,default=0)
    Latitude = models.FloatField(max_length=8,default=30)
    Longitude = models.FloatField(max_length=8,default=-8)

    object= GeoManager()

    def save(self, *args, **kwargs):
         self.Latitude  = self.geom.y
         self.Longitude = self.geom.x
         super(Etablissements, self).save(*args, **kwargs)


#    def __str__(self):
#         return self.Nom
