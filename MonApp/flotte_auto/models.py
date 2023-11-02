from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
from django.db import models




class Vehicule(models.Model):
    marque = models.CharField(max_length=255)
    modele = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    annee_fabrication = models.PositiveIntegerField()
    numéro_immatriculation = models.CharField(max_length=20, unique=True)
    kilometrage = models.PositiveIntegerField()
    typeCarburant=models.CharField(max_length=20,choices=([('Gazoil','gazoil'),('Essence','essence')]))
    STATUT_CHOICES = (
        ('Disponible', 'Disponible'),
        ('En Entretien', 'En Entretien'),
        ('Réservé', 'Réservé'),
        ('Indisponible', 'Indisponible'),
        
    )
    
    statut = models.CharField(max_length=20, choices=STATUT_CHOICES, default='Disponible')
    
    
    @classmethod
    def vehicules_disponibles(cls):
        return cls.objects.filter(statut='Disponible')

    @classmethod
    def vehicules_en_entretien(cls):
        return cls.objects.filter(statut='En Entretien')

    @classmethod
    def vehicules_reserve(cls):
        return cls.objects.filter(statut='Reserve')
    
    
    

    def assurances_actives(self):
        today = timezone.now().date()
        return self.assurance_set.filter(date_debut__lte=today, date_fin__gte=today)


    def __str__(self):
        return self.modele + self.marque


##########################################################
#Utilisateurs
##########################################################

class GestionnaireParc(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    numéro_bureau = models.CharField(max_length=20)
    date_embauche = models.DateField()
    telephone=models.IntegerField()
    adresse=models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    def __str__(self):
        return self.utilisateur.first_name
     
    
    
class GestionnaireConsommation(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    département = models.CharField(max_length=255)
    date_embauche = models.DateField()
    telephone=models.IntegerField()
    adresse=models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    
    def __str__(self):
        return self.utilisateur.first_name


class GestionnaireIntervention(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    service = models.CharField(max_length=255)
    date_embauche = models.DateField()
    telephone=models.IntegerField()
    adresse=models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    def __str__(self):
        return self.utilisateur.first_name


class Employé(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    telephone=models.IntegerField()
    adresse=models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    reservations = models.ManyToManyField('ReservationVoiture', blank=True)  # Relation many-to-many
    
    def __str__(self):
        return self.utilisateur.first_name
    
#####################################
##
#####################################




class ReservationVoiture(models.Model):
    employe = models.ForeignKey(User, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True,null=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    destination = models.CharField(max_length=200)
    motif = models.TextField()
    statut = models.CharField(max_length=20, default='En attente')  # Statut de la réservation (En attente/Validée/Refusée)
    vehicules = models.ManyToManyField(Vehicule)  # Véhicule réservé (peut être vide si en attente)
    # Autres champs au besoin

    
    def __str__(self):
        return self.employe.username




from datetime import timedelta

class Maintenance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_maintenance = models.DateTimeField()
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    prochaine_maintenance = models.DateTimeField()  # Ajoutez ce champ
    
    def save(self, *args, **kwargs):
        # Calculez la date de la prochaine maintenance en ajoutant 1 mois à la date actuelle
        self.prochaine_maintenance = self.date_maintenance + timedelta(days=30)
        super(Maintenance, self).save(*args, **kwargs)



class Conducteur(models.Model):
    prenom = models.CharField(max_length=255)
    nom = models.CharField(max_length=255)
    numero_permis_conduire = models.CharField(max_length=20, unique=True)
    horaires_travail = models.TextField()
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)
    telephone=models.IntegerField()
    
    def __str__(self):
        return self.prenom + self.nom
    



class Itineraire(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    date_depart = models.DateTimeField()
    date_arrivee = models.DateTimeField()
    lieu_depart = models.CharField(max_length=255)
    lieu_arrivee = models.CharField(max_length=255)



class PerformanceConduite(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()

class Notification(models.Model):
    type_notification = models.CharField(max_length=255)
    message = models.TextField()
    date_envoi = models.DateTimeField()
    destinataire = models.ForeignKey(User, on_delete=models.CASCADE)


#modèle pour gérer les coûts liés à la flotte automobile, 
# y compris les coûts d'acquisition, d'entretien, 
# de carburant, d'assurance, etc.
class Cout(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    type_cout = models.CharField(max_length=255)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    description = models.TextField()
    
    
    
class DonnéesConsommationCarburant(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date = models.DateField()
    quantité_carburant = models.DecimalField(max_digits=8, decimal_places=2)
    gestionnaire_consommation = models.ForeignKey(GestionnaireConsommation, on_delete=models.CASCADE)



class NoteConducteur(models.Model):
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire=models.TextField()
    
class Assurance(models.Model):
    vehicule = models.ForeignKey('Vehicule', on_delete=models.CASCADE)
    compagnie_assurance = models.CharField(max_length=100)
    numero_police = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prime_annuelle = models.DecimalField(max_digits=10, decimal_places=2)
    statut=models.CharField(max_length=50, default='Valide')

    def __str__(self):
        return f"Assurance de {self.vehicule} ({self.compagnie_assurance})"
