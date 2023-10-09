from django.contrib import admin
from .models import *

# Enregistrez les modèles dans l'administration Django
admin.site.register(Vehicule)
admin.site.register(GestionnaireParc)
admin.site.register(GestionnaireConsommation)
admin.site.register(GestionnaireIntervention)
admin.site.register(Employé)
admin.site.register(ReservationVoiture)
admin.site.register(Maintenance)
admin.site.register(Conducteur)
admin.site.register(Itineraire)
admin.site.register(PerformanceConduite)
admin.site.register(Notification)
admin.site.register(Cout)
admin.site.register(DonnéesConsommationCarburant)

# Assurez-vous d'enregistrer tous les modèles que vous souhaitez gérer dans l'interface d'administration.




# Register your models here.
