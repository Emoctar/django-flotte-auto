from flotte_auto.models import * 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *
from django.urls import reverse
from .utils import*

from django.conf import settings

#####################################################################
# views.py


from .tasks import *

def task_results(request):
    # Appelez votre tâche Celery pour obtenir les résultats
    result = mettre_a_jour_statut_vehicules_task.delay()

    # Récupérez le résultat de la tâche
    task_result = result.get()

    # Passez le résultat au modèle
    return render(request, 'task_results.html', {'task_result': task_result})

############################################
#Compteur nbr_notif GesParc

def compteur(request):
    # Récupérez le nombre de réservations
    nombre_reservations = ReservationVoiture.objects.count()

    # Passez le nombre de réservations au modèle HTML
    return render(request, 'GesParc/home_GesParc.html', {'nombre_reservations': nombre_reservations})




######################################################################

 
def index(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'Accueil/index.html', {'vehicules': vehicules})

################################################################
#NOTATION






######################################################
#VOITURES

@login_required
def creer_vehicule(request):
    """Vue pour créer un nouveau véhicule dans la flotte."""
    if request.method == 'POST':
        form = VehiculeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_vehicules')
    else:
        form = VehiculeForm()
    
    return render(request, 'GesParc/creer_vehicules.html', {'form': form})

@login_required
def modifier_vehicule(request, vehicule_id):
    """Vue pour modifier les détails d'un véhicule existant."""
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)

    if request.method == 'POST':
        form = VehiculeForm(request.POST,request.FILES, instance=vehicule)
        if form.is_valid():
            form.save()
            return redirect(reverse('modifier_vehicule', args=[vehicule_id]))

    form = VehiculeForm(instance=vehicule)
    return render(request, 'GesParc/modifier_vehicule.html', {'form': form, 'vehicule': vehicule})

@login_required
def supprimer_vehicule(request, vehicule_id):
    """Vue pour supprimer un véhicule de la flotte."""
    vehicule = get_object_or_404(Vehicule, id=vehicule_id)
    
    if request.method == 'POST':
        vehicule.delete()
        return redirect('liste_vehicules')

    return render(request, 'supprimer_vehicule.html', {'vehicule': vehicule})

@login_required
def liste_vehicules_disponible(request):
    """Vue pour afficher la liste des véhicules de la flotte."""
    vehicules = Vehicule.vehicules_disponibles()
    return render(request, 'Employe/liste_voitures_disponible.html', {'vehicules': vehicules})


def liste_vehicules(request):
    """Vue pour afficher la liste des véhicules de la flotte."""
    vehicules = Vehicule.objects.all()
    return render(request, 'GesParc/liste_vehicules.html', {'vehicules': vehicules})



def details_vehicule(request, vehicule_id):
    # Récupérer la voiture à l'aide de l'ID fourni ou afficher une erreur 404 si elle n'existe pas
    vehicules = get_object_or_404(Vehicule, id=vehicule_id)

    return render(request, 'Employe/details_vehicule.html', {'vehicule': vehicules})



#####################################################################################

#CONDUCTEURS

@login_required
def creer_conducteur(request):
    """Vue pour créer un nouveau conducteur."""
    if request.method == 'POST':
        form = ConducteurForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_conducteurs')
    else:
        form = ConducteurForm()
    
    return render(request, 'Chauffeur/ajouter_conducteur.html', {'form': form})

@login_required
def modifier_conducteur(request, conducteur_id):
    #Vue pour modifier les détails d'un conducteur existant."""
    conducteur = get_object_or_404(Conducteur, id=conducteur_id)

    if request.method == 'POST':
        form = ConducteurForm(request.POST,request.FILES, instance=conducteur)
        if form.is_valid():
            form.save()
            return redirect('liste_conducteurs')

    form = ConducteurForm(instance=conducteur)
    return render(request, 'Chauffeur/modifier_conducteur.html', {'form': form, 'conducteur': conducteur})

@login_required
def supprimer_conducteur(request, conducteur_id):
     #Vue pour supprimer un conducteur.
    conducteur = get_object_or_404(Conducteur, id=conducteur_id)
    
    if request.method == 'POST':
        conducteur.delete()
        return redirect('liste_conducteurs')

    return render(request, 'Chauffeur/supprimer_conducteur.html', {'conducteur': conducteur})



@login_required
def liste_conducteurs(request):
    #Vue pour afficher la liste des conducteurs."""
    conducteurs = Conducteur.objects.all()
    return render(request, 'Chauffeur/liste_conducteur.html', {'conducteurs': conducteurs})

##########################################
#RESERVATION



def gerer_reservations_attente(request):
    # Récupérez toutes les réservations en attente depuis la base de données
    reservations_attente = ReservationVoiture.objects.filter(statut='En attente').order_by('date_demande')
    
    # Affichez ces réservations en attente dans un modèle approprié
    return render(request, 'GesParc/gerer_reservations_attente.html', {'reservations_attente': reservations_attente})


def gerer_reservations_accepter(request):
    # Récupérez toutes les réservations validées depuis la base de données
    reservations_valide = ReservationVoiture.objects.filter(statut='Validée')
 
    # Affichez ces réservations validées dans un modèle approprié
    return render(request, 'GesParc/reservation_valide.html', {'reservations_valide': reservations_valide})

def gerer_reservations_refuse(request):
    # Récupérez toutes les réservations refusées depuis la base de données
    reservations_refuse = ReservationVoiture.objects.filter(statut='Refusée')
    
    # Affichez ces réservations refusées dans un modèle approprié
    return render(request, 'GesParc/refus_reservation.html', {'reservations_refuse': reservations_refuse})


from django.shortcuts import get_object_or_404, redirect, render
from .models import ReservationVoiture
from .utils import envoyer_email_notification  # Assurez-vous d'importer cette fonction depuis vos utilitaires

def valider_reservation(request, reservation_id):
    # Récupérez la réservation en fonction de l'ID
    reservation = get_object_or_404(ReservationVoiture, id=reservation_id)

    if request.method == 'POST' :
        # Marquez la réservation comme validée
        reservation.statut = 'Validée'
        
        reservation.save()

        # Récupérez les détails des véhicules associés à la réservation
        vehicules_reserves = reservation.vehicules.all()
        
        for vehicule in vehicules_reserves:
            vehicule.statut = 'Réservé'
            vehicule.save()

        # Personnalisez le sujet et le message ici avec les détails de la réservation
        sujet = 'Réservation validée'
        message = f'Votre réservation a été validée avec succès.\n\nDétails de la réservation :\n'
        message += f'Date de début : {reservation.date_debut}\n'
        message += f'Date de fin : {reservation.date_fin}\n'
        message += f'Destination : {reservation.destination}\n'
        message += f'Motif : {reservation.motif}\n'

        # Ajoutez les détails des véhicules réservés au message
        message += 'Véhicules réservés :\n'
        for vehicule in vehicules_reserves:
            message += f'Marque : {vehicule.marque}, Modèle : {vehicule.modele}, Plaque d\'immatriculation : {vehicule.numéro_immatriculation}\n'

        destinataires = [reservation.employe.email]


        try:
            envoyer_email_notification(sujet, message, destinataires)
            messages.success(request, "L'e-mail a été envoyé avec succès.")
        except Exception as e:
             messages.error(request, f"Erreur lors de l'envoi de l'e-mail : {e}")

      

    return render(request, 'GesParc/confirmation_validation.html', {'reservation': reservation})  # Remplacez 'template.html' par le nom de votre modèle HTML


def confirmation_validation(request):
    return render(request, 'GesParc/confirmation_validation.html')

from django.contrib import messages
def refuser_reservation(request, reservation_id):
    # Récupérez la réservation en fonction de l'ID
    reservation = get_object_or_404(ReservationVoiture, id=reservation_id)

    if request.method == 'POST':
        # Marquez la réservation comme refusée
        reservation.statut = 'Refusée'

        # Récupérez le motif de refus à partir du formulaire
        motif_refus = request.POST.get('motif_refus', '')

        # Si un motif de refus est fourni, ajoutez-le au message
        if motif_refus:
            message = f"La réservation a été refusée pour la raison suivante : {motif_refus}"
        else:
            message = "La réservation a été refusée."

        # Sauvegarder la réservation et envoyer un message de confirmation
        reservation.save()
        messages.success(request, message)

        # Envoyer un e-mail pour informer l'utilisateur de la réservation refusée
        sujet = "Réservation refusée"
        message_email = f"Votre réservation a été refusée pour la raison suivante : {motif_refus}" if motif_refus else "Votre réservation a été refusée."
        destinataires = [reservation.employe.email]  # Modifier en conséquence pour obtenir l'adresse e-mail de l'employé
        try:
            envoyer_email_notification(sujet, message_email, destinataires)
        except Exception as e:
            messages.error(request, f"Erreur lors de l'envoi de l'e-mail : {e}")

        # Rediriger l'utilisateur vers une page de confirmation ou ailleurs
        return redirect('gerer_reservations_attente')

    return render(request, 'GesParc/details_reservation.html', {'reservation': reservation})




# views.py

from .utils import envoyer_sms

from django.contrib import messages


@login_required
def creer_reservation(request):
    if request.method == 'POST':
        form = ReservationVoitureForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.employe = request.user
            reservation.save()  # Enregistrez la réservation

            # Récupérez les véhicules sélectionnés dans le formulaire
            vehicules_selectionnes = form.cleaned_data['vehicules']

            # Associez les véhicules à la réservation
            reservation.vehicules.set(vehicules_selectionnes)

            messages.success(request, "Votre réservation a été créée avec succès.")
            return redirect('creer_reservation')
        else:
            messages.error(request, "Vous ne pouvez sélectionner que 3 véhicules au maximum. .")
    else:
        form = ReservationVoitureForm()

    return render(request, 'Employe/creer_reservation.html', {'form': form})

    
@login_required
def modifier_reservation(request, reservation_id):
    #Vue pour modifier les détails d'une réservation de voiture existante."""
    reservation = get_object_or_404(ReservationVoiture, id=reservation_id)

    if request.method == 'POST':
        form = ReservationVoitureForm(request.POST, instance=reservation)
        if form.is_valid():
            form.save()
            return redirect('details_reservation')

    form = ReservationVoitureForm(instance=reservation)
    
    return render(request, 'Employe/modifier_reservation.html', {'form': form, 'reservation': reservation})

@login_required
def supprimer_reservation(request, reservation_id):
    #Vue pour supprimer une réservation de voiture."""
    reservation = get_object_or_404(ReservationVoiture, id=reservation_id)
    
    if request.method == 'POST':
        reservation.delete()
        return redirect('liste_reservations')

    return render(request, 'supprimer_reservation.html', {'reservation': reservation})

@login_required
def liste_reservations(request):
    #Vue pour afficher la liste des réservations de voiture."""
    reservations = ReservationVoiture.objects.all()
    return render(request, 'liste_reservations.html', {'reservations': reservations})


def details_reservation(request, reservation_id):
    reservation = get_object_or_404(ReservationVoiture, id=reservation_id)
    
    # Utilisez le contexte pour avoir accès à ces informations
    demandeur = reservation.employe # Récupérez les informations du demandeur
    vehicules_reserves = reservation.vehicules.all() if reservation.vehicules else []  # Récupérez les véhicules réservés

    print("Informations de l'employé : ", demandeur)  # Ajoutez des déclarations de débogage
    print("Nom de l'employé : ", demandeur.username)  # Assurez-vous que les attributs de l'employé sont accessibles

    context = {
        'reservation': reservation,
        'demandeur': demandeur,
        'vehicules_reserves': vehicules_reserves,
    }

    return render(request, 'GesParc/details_reservation.html', context)







######################################################################
#ENTRETIEN
@login_required
def ajouter_maintenance(request):
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            
            # Obtenez l'ID du véhicule sélectionné à partir du formulaire
            vehicule_id = form.cleaned_data['vehicule'].id
            
            # Récupérez l'instance du modèle Vehicule correspondante
            vehicule = get_object_or_404(Vehicule, pk=vehicule_id)
            
            # Assurez-vous que le véhicule est disponible
            if vehicule.vehicules_disponibles():
                maintenance.vehicule = vehicule
                
                # Calculer la prochaine maintenance prévue
                maintenance.prochaine_maintenance = maintenance.date_maintenance + timedelta(days=30)
                
                maintenance.save()
                messages.success(request, 'Maintenance ajoutée avec succès.')
                
                # Changez automatiquement le statut du véhicule en 'En Entretien'
                vehicule.statut = 'En Entretien'
                vehicule.save()
                
                return redirect('liste_vehicules')  # Rediriger vers la liste des véhicules
            else:
                messages.error(request, 'Le véhicule sélectionné n\'est pas disponible.')
    else:
        form = MaintenanceForm()
    
    return render(request, 'GesIntervention/ajouter_maintenance.html', {'form': form})

@login_required
def modifier_maintenance(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)

    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Maintenance modifiée avec succès.')
            return redirect('liste_maintenance')
    else:
        form = MaintenanceForm(instance=maintenance)

    return render(request, 'GesIntervention/modifier_maintenance.html', {'form': form, 'maintenance': maintenance})

@login_required
def supprimer_maintenance(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)

    if request.method == 'POST':
        maintenance.delete()
        messages.success(request, 'Maintenance supprimée avec succès.')
        return redirect('liste_maintenance')

    return render(request, 'GesIntervention/supprimer_maintenance.html', {'maintenance': maintenance})

##########################################################################

from django.utils import timezone
@login_required
def liste_maintenance(request):
    # Obtenez la date actuelle
    today = timezone.now().date()
    
    # Obtenez toutes les maintenances dont la date de prochaine maintenance est aujourd'hui ou avant
    maintenances = Maintenance.objects.all()
    
    return render(request, 'GesIntervention/liste_maintenance.html', {'maintenances': maintenances})


#ITINERAIRE

def creer_itineraire(request):
    if request.method == 'POST':
        form = ItineraireForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_itineraires')
    else:
        form = ItineraireForm()
    
    vehicules = Vehicule.objects.all()
    conducteurs = Conducteur.objects.all()
    return render(request, 'creer_itineraire.html', {'form': form, 'vehicules': vehicules, 'conducteurs': conducteurs})

def modifier_itineraire(request, itineraire_id):
    itineraire = get_object_or_404(Itineraire, id=itineraire_id)

    if request.method == 'POST':
        form = ItineraireForm(request.POST, instance=itineraire)
        if form.is_valid():
            form.save()
            return redirect('liste_itineraires')

    form = ItineraireForm(instance=itineraire)
    vehicules = Vehicule.objects.all()
    conducteurs = Conducteur.objects.all()
    return render(request, 'modifier_itineraire.html', {'form': form, 'itineraire': itineraire, 'vehicules': vehicules, 'conducteurs': conducteurs})

def supprimer_itineraire(request, itineraire_id):
    itineraire = get_object_or_404(Itineraire, id=itineraire_id)
    
    if request.method == 'POST':
        itineraire.delete()
        return redirect('liste_itineraires')

    return render(request, 'supprimer_itineraire.html', {'itineraire': itineraire})

def liste_itineraires(request):
    itineraires = Itineraire.objects.all()
    return render(request, 'liste_itineraires.html', {'itineraires': itineraires})

############################################################

@login_required
def noter_conducteur(request, conducteur_id):
    conducteur = get_object_or_404(Conducteur, id=conducteur_id)
    utilisateur = request.user

    if request.method == 'POST':
        form = NoteConducteurForm(request.POST)
        if form.is_valid():
            note = form.save(commit=False)
            note.conducteur = conducteur
            note.utilisateur = utilisateur
            note.save()
            return redirect('liste_conducteurs')

    else:
        form = NoteConducteurForm()

    return render(request, 'Chauffeur/noter_conducteur.html', {'form': form, 'conducteur': conducteur})
###################################################################
#CONSOMMATION

def enregistrer_donnees_consommation(request):
    if request.method == 'POST':
        form = ConsommationCarburantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_donnees_consommation_carburant')
    else:
        form = ConsommationCarburantForm()
    
    vehicules = Vehicule.objects.all()
    
    return render(request, 'GesParc/enregistrer_données_consommation.html', {'form': form, 'vehicules': vehicules})

# # Vue pour modifier les données de consommation de carburant existantes
def modifier_données_consommation(request, données_consommation_id):
    donnees_consommation = get_object_or_404(ConsommationCarburantForm, id=données_consommation_id)

    if request.method == 'POST':
        form = ConsommationCarburantForm(request.POST, instance=donnees_consommation)
        if form.is_valid():
            form.save()
            return redirect('liste_données_consommation_carburant')

    form = ConsommationCarburantForm(instance=donnees_consommation)
    vehicules = Vehicule.objects.all()
    gestionnaires_consommation = GestionnaireConsommation.objects.all()
    return render(request, 'modifier_données_consommation.html', {'form': form, 'donnees_consommation': donnees_consommation, 'vehicules': vehicules, 'gestionnaires_consommation': gestionnaires_consommation})

# # Vue pour supprimer un enregistrement de données de consommation de carburant
def supprimer_donnees_consommation(request, données_consommation_id):
    données_consommation = get_object_or_404(ConsommationCarburantForm, id=données_consommation_id)
    
    if request.method == 'POST':
        données_consommation.delete()
        return redirect('liste_données_consommation_carburant')

    return render(request, 'supprimer_données_consommation.html', {'données_consommation': données_consommation})

# # Vue pour afficher la liste des données de consommation de carburant
@login_required
def liste_donnees_consommation_carburant(request):
    donnees_consommation = ConsommationCarburant.objects.all()
    return render(request, 'GesParc/liste_données_consommation_carburant.html', {'donnees_consommation': donnees_consommation})



def suivi_consommation(request):
    vehicules = Vehicule.objects.all()
    context = {
        'vehicules': vehicules
    }
    return render(request, 'GesParc/suivi_consommation.html', context)

from django.http import JsonResponse,HttpResponse

# def suivi_consommation(request):
#     if request.method == 'POST':
#         # Traitez les données de formulaire et calculez le taux de consommation
#         form = SearchForm(request.POST)
#         if form.is_valid():
#             start_date = form.cleaned_data['start_date']
#             end_date = form.cleaned_data['end_date']
#             vehicle = form.cleaned_data['vehicle']

#             if vehicle:
#                 consumption_rate = vehicle.consommation_moyenne(start_date, end_date)
#             else:
#                 # Calculer la moyenne de consommation pour tous les véhicules
#                 vehicles = Vehicule.objects.all()
#                 total_consumption_rate = sum(vehicle.consommation_moyenne(start_date, end_date) for vehicle in vehicles)
#                 consumption_rate = total_consumption_rate / len(vehicles) if vehicles else 0

#             return JsonResponse({'consumption_rate': consumption_rate})

#         return HttpResponse(status=400)  # Bad Request

#     # Le reste de la logique de vue, par exemple la création d'un formulaire et l'affichage de la page
#     form = SearchForm()
#     return render(request, 'GesParc/suivi_consommation.html', {'form': form})

# ############################################################
#COUT

    #Vue pour enregistrer un coût lié à la flotte automobile
def enregistrer_cout(request):
    if request.method == 'POST':
        form = CoutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_couts')
    else:
        form = CoutForm()
    
    vehicules = Vehicule.objects.all()
    return render(request, 'enregistrer_cout.html', {'form': form, 'vehicules': vehicules})

# Vue pour modifier les informations sur un coût existant
def modifier_cout(request, cout_id):
    cout = get_object_or_404(Cout, id=cout_id)

    if request.method == 'POST':
        form = CoutForm(request.POST, instance=cout)
        if form.is_valid():
            form.save()
            return redirect('liste_couts')

    form = CoutForm(instance=cout)
    vehicules = Vehicule.objects.all()
    return render(request, 'modifier_cout.html', {'form': form, 'cout': cout, 'vehicules': vehicules})

# Vue pour supprimer un enregistrement de coût
def supprimer_cout(request, cout_id):
    cout = get_object_or_404(Cout, id=cout_id)
    
    if request.method == 'POST':
        cout.delete()
        return redirect('liste_couts')

    return render(request, 'supprimer_cout.html', {'cout': cout})

# Vue pour afficher la liste des coûts
def liste_couts(request):
    couts = Cout.objects.all()
    return render(request, 'liste_couts.html', {'couts': couts})




#############################################################
#Notifications

# Vue pour créer une notification
def creer_notification(request):
    if request.method == 'POST':
        form = NotificationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_notifications')
    else:
        form = NotificationForm()
    
    conducteurs = Conducteur.objects.all()
    gestionnaires = [GestionnaireParc, GestionnaireConsommation, GestionnaireIntervention]  # Mettez ici les gestionnaires nécessaires
    return render(request, 'creer_notification.html', {'form': form, 'conducteurs': conducteurs, 'gestionnaires': gestionnaires})

# Vue pour modifier le contenu d'une notification existante
def modifier_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)

    if request.method == 'POST':
        form = NotificationForm(request.POST, instance=notification)
        if form.is_valid():
            form.save()
            return redirect('liste_notifications')

    form = NotificationForm(instance=notification)
    conducteurs = Conducteur.objects.all()
    gestionnaires = [GestionnaireParc, GestionnaireConsommation, GestionnaireIntervention]  # Mettez ici les gestionnaires nécessaires
    return render(request, 'modifier_notification.html', {'form': form, 'notification': notification, 'conducteurs': conducteurs, 'gestionnaires': gestionnaires})

# Vue pour supprimer une notification
def supprimer_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    
    if request.method == 'POST':
        notification.delete()
        return redirect('liste_notifications')

    return render(request, 'supprimer_notification.html', {'notification': notification})

# Vue pour afficher la liste des notifications
def liste_notifications(request):
    notifications = Notification.objects.all()
    return render(request, 'liste_notifications.html', {'notifications': notifications})


#Vue pour Assurrance

def ajouter_assurance(request, vehicule_id):
    vehicule = Vehicule.objects.get(pk=vehicule_id)

    if request.method == 'POST':
        form = AssuranceForm(request.POST)  # Créez une instance du formulaire avec les données POST

        if form.is_valid():
            assurance = form.save(commit=False)
            assurance.vehicule = vehicule  # Liez l'assurance au véhicule
            assurance.save()
            return redirect('liste_vehicules')
    else:
        form = AssuranceForm()

    return render(request, 'Assurance/assurances.html', {'vehicule': vehicule, 'form': form})


def mettre_a_jour_statut_vehicules(request):
    # Récupérer toutes les assurances expirées
    assurances_expirees = Assurance.objects.filter(date_fin__lt=timezone.now().date())

    # Mettre à jour le statut des véhicules associés aux assurances expirées
    for assurance in assurances_expirees:
        vehicule = assurance.vehicule
        vehicule.statut = 'Indisponible'
        vehicule.save()

    return redirect('liste_vehicules')


def liste_assurances(request):
    assurances = Assurance.objects.all()
    context = {'assurances': assurances}
    return render(request, 'Assurance/liste_assurances.html', context)


from django.shortcuts import render

def ma_vue(request):
    # Récupérer l'utilisateur connecté
    utilisateur_connecte = request.user
    
    # Vérifier s'il a un gestionnaire de parc associé
    if hasattr(utilisateur_connecte, 'GestionnaireParc'):
        gestionnaire_parc = utilisateur_connecte.GestionnaireParc
    else:
        gestionnaire_parc = None
    
    context = {
        'gestionnaire_parc': gestionnaire_parc,
    }
    
    return render(request, 'GesParc/home_GesParc.html', context)

