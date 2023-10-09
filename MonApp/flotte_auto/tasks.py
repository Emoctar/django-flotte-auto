# tasks.py

from celery import shared_task
from django.shortcuts import redirect
from django.utils import timezone
from .models import *
from celery import shared_task

from django.contrib.auth.models import User

@shared_task
def mettre_a_jour_statut_vehicules_task():
    # Récupérer toutes les assurances expirées
    assurances_expirees = Assurance.objects.filter(date_fin__lt=timezone.now().date())

    # Mettre à jour le statut des véhicules associés aux assurances expirées
    for assurance in assurances_expirees:
        vehicule = assurance.vehicule
        vehicule.statut = 'Indisponible'
        vehicule.save()


# @shared_task
# def notifier_entretien_planifie():
#     # Obtenez la date actuelle
#     today = timezone.now().date()

#     # Obtenez tous les véhicules dont la date de prochaine maintenance est aujourd'hui ou avant
#     vehicules_en_entretien = Vehicule.objects.filter(maintenance__prochaine_maintenance__lte=today)

#     for vehicule in vehicules_en_entretien:
#         # Envoyez une notification par e-mail au gestionnaire de parc
#         gestionnaire_de_parc = User.objects.get(username='ephia@gmail.com')
#         destinataires = [gestionnaire_de_parc.email]
#         sujet = f"Entretien planifié pour {vehicule}"
#         contenu = f"Le véhicule {vehicule} nécessite un entretien."
#         envoyer_email_sujet_contenu(destinataires, sujet, contenu)
        
#         # Changez automatiquement le statut du véhicule en 'En Entretien'
#         vehicule.statut = 'En Entretien'
#         vehicule.save()
# Assurez-vous d'activer Celery Beat : Vous devez exécuter Celery Beat pour planifier la tâche notifier_entretien_planifie à intervalles réguliers. Vous pouvez le faire avec la commande suivante :
# bash
# Copy code
# celery -A votre_projet beat --loglevel=info
# Créez un modèle pour stocker les notifications (optionnel) : Si vous souhaitez conserver un historique des notifications, vous pouvez créer un modèle dans votre application pour enregistrer les notifications envoyées.

# Configurez le gestionnaire de parc : Le gestionnaire de parc doit avoir un compte d'utilisateur dans votre application Django, et son adresse e-mail doit être configurée pour recevoir des notifications.

# Avec cette configuration, chaque fois qu'une maintenance est planifiée, le gestionnaire de parc recevra une notification par e-mail l'informant de la maintenance à venir.






