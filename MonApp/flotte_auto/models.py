from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db import models

class Assurance(models.Model):
    
    CHOIX_COMPAGNIE = (
        ('Axa', 'Axa'),
        ('NSIA', 'NSIA'),
        ('CNART', 'CNART'),
        ('SenAssurance', 'SenAssurance'),
    )
    compagnie_assurance = models.CharField(max_length=100, choices=CHOIX_COMPAGNIE)
    numero_police = models.CharField(max_length=50)
    date_debut = models.DateField()
    date_fin = models.DateField()
    prime_annuelle = models.DecimalField(max_digits=10, decimal_places=2)
    statut=models.CharField(max_length=50, default='Valide')

    def __str__(self):
        return f"Assurance de {self.compagnie_assurance}"



class Vehicule(models.Model):
    assurance = models.ForeignKey(Assurance, on_delete=models.CASCADE)
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
        return cls.objects.filter(statut='Réservé')
    
    
    

    def assurances_actives(self):
        today = timezone.now().date()
        return self.assurance_set.filter(date_debut__lte=today, date_fin__gte=today)


    def __str__(self):
        return self.modele + self.marque
    
    
    def consommation_moyenne(self):
        consommations = ConsommationCarburant.objects.filter(vehicule=self)
        if consommations.exists():
            quantite_totale = sum([consommation.quantite_carburant for consommation in consommations])
            distance_totale = sum([consommation.distance_parcourue for consommation in consommations])
            if distance_totale > 0:
                return quantite_totale / distance_totale
        return 0 
    
  
        
    def en_maintenance(self):
        return self.maintenance_set.filter(vehicule=self, en_cours=True).exists()
    
    def en_panne(self):
        return self.panne_set.filter(statut='En cours').exists()



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



#####################################
##
#####################################




class ReservationVoiture(models.Model):
    employe = models.ForeignKey(User, on_delete=models.CASCADE)
    date_demande = models.DateTimeField(auto_now_add=True,null=True)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    REGIONS_CHOICES = [
        ('Dakar', 'Dakar'),
        ('Diourbel', 'Diourbel'),
        ('Fatick', 'Fatick'),
        ('Kaffrine', 'Kaffrine'),
        ('Kaolack', 'Kaolack'),
        ('Kédougou', 'Kédougou'),
        ('Kolda', 'Kolda'),
        ('Louga', 'Louga'),
        ('Matam', 'Matam'),
        ('Saint-Louis', 'Saint-Louis'),
        ('Sédhiou', 'Sédhiou'),
        ('Tambacounda', 'Tambacounda'),
        ('Thiès', 'Thiès'),
        ('Ziguinchor', 'Ziguinchor'),
    ]

    destination = models.CharField(max_length=200, choices=REGIONS_CHOICES)
    motif = models.TextField()
    statut = models.CharField(max_length=20, default='En attente')  # Statut de la réservation (En attente/Validée/Refusée)
    vehicules = models.ManyToManyField(Vehicule)  # Véhicule réservé (peut être vide si en attente)
    # Autres champs au besoin

    
    def __str__(self):
        return self.employe.username
    
    @staticmethod
    def reservations_acceptees():
        return ReservationVoiture.objects.filter(statut='Validée')

    @staticmethod
    def reservations_refusees():
        return ReservationVoiture.objects.filter(statut='Refusée')
    
    
    
class Employé(models.Model):
    utilisateur = models.OneToOneField(User, on_delete=models.CASCADE)
    poste = models.CharField(max_length=255)
    departement = models.CharField(max_length=255)
    telephone=models.IntegerField()
    adresse=models.CharField(max_length=120)
    photo = models.ImageField(upload_to='photos/', blank=True, null=True)

    def __str__(self):
        return self.utilisateur.first_name
    




from datetime import timedelta

class Maintenance(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    date_maintenance = models.DateTimeField()
    description = models.TextField()
    cout = models.DecimalField(max_digits=10, decimal_places=2)
    prochaine_maintenance = models.DateTimeField()  # Ajoutez ce champ
    en_cours = models.BooleanField(default=True)
                                   
                    
    
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
    





    
    
class ConsommationCarburant(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    reservation = models.ForeignKey(ReservationVoiture, on_delete=models.CASCADE)
    date = models.DateField()
    quantite_carburant = models.DecimalField(max_digits=6, decimal_places=2)  # En litres
    distance_parcourue = models.DecimalField(max_digits=6, decimal_places=2)  # En kilomètres
  




class Panne(models.Model):
    vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    description = models.TextField()
    date_signalement = models.DateTimeField(auto_now_add=True)
    date_fin_intervention = models.DateTimeField(blank=True, null=True)
    TYPE_PANNE_CHOICES = [
        ('Mécanique', 'Mécanique'),
        ('Electrique', 'Electrique'),
        ('Pneumatique', 'Pneumatique'),
        ('Carrosserie', 'Carrosserie'),
        ('Système de freinage', 'Système de freinage'),
        ('Système de transmission', 'Système de transmission'),
        ('Climatisation', 'Climatisation'),
        ('Système de refroidissement', 'Système de refroidissement'),
        ('Autre', 'Autre'),
    ]
    type_panne = models.CharField(max_length=30, choices=TYPE_PANNE_CHOICES, default='Autre')
    statut = models.CharField(max_length=20, default='En cours')  # Statut de la panne (En cours/Cloture)
    commentaire = models.TextField(blank=True, null=True)
    conducteur = models.ForeignKey(Conducteur, on_delete=models.CASCADE, blank=True, null=True)


    def marquer_en_cours(self):
        self.statut = 'En cours'
        self.save()

    def marquer_resolue(self):
        self.statut = 'Résolue' 
        self.date_fin_intervention = timezone.now()
        self.save()
        
        
        
