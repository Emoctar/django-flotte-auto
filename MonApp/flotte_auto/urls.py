from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views


urlpatterns = [
    
    ###########################################
     path('task_results/', views.task_results, name='task_results'),
    
    #######################3
    
    path('', views.index, name='index'),
    
    # path('home/', views.home, name='home'),
    # URLs pour les modèles Vehicule, GestionnaireParc, GestionnaireConsommation, GestionnaireIntervention, Employé
   path('gestionnaire_parc_profile/creer_vehicule/', views.creer_vehicule, name='creer_vehicule'),
    path('gestionnaire_parc_profile/modifier_vehicule/<int:vehicule_id>/', views.modifier_vehicule, name='modifier_vehicule'),
    path('gestionnaire_parc_profile/supprimer_vehicule/<int:vehicule_id>/', views.supprimer_vehicule, name='supprimer_vehicule'),
    path('liste_vehicules/', views.liste_vehicules, name='liste_vehicules'),
     path('vehicule/<int:vehicule_id>/', views.details_vehicule, name='details_vehicule'),

    # Vues liées aux conducteurs
    path('gestionnaire_parc_profile/creer_conducteur/', views.creer_conducteur, name='creer_conducteur'),
    path('gestionnaire_parc_profile/modifier_conducteur/<int:conducteur_id>/', views.modifier_conducteur, name='modifier_conducteur'),
    path('gestionnaire_parc_profile/supprimer_conducteur/<int:conducteur_id>/', views.supprimer_conducteur, name='supprimer_conducteur'),
    path('gestionnaire_parc_profile/liste_conducteurs/', views.liste_conducteurs, name='liste_conducteurs'),

    # Vues liées aux réservations
    path('employe_profile/creer_reservation/', views.creer_reservation, name='creer_reservation'),
    path('employe_profile/modifier_reservation/<int:reservation_id>/', views.modifier_reservation, name='modifier_reservation'),
    path('employe_profile/supprimer_reservation/<int:reservation_id>/', views.supprimer_reservation, name='supprimer_reservation'),
    path('liste_reservations/', views.liste_reservations, name='liste_reservations'),
    path('employe_profile/liste_vehicules_disponible', views.liste_vehicules_disponible, name='liste_vehicules_disponible'),
    path('employe_profile/noter/<int:conducteur_id>/', views.noter_conducteur, name='noter_conducteur'),
    path('gestionnaire_parc_profile/gerer_reservations_attente/', views.gerer_reservations_attente, name='gerer_reservations_attente'),
    path('gestionnaire_parc_profile/valider_reservation/<int:reservation_id>/', views.valider_reservation, name='valider_reservation'),
    path('gestionnaire_parc_profile/refuser_reservation/<int:reservation_id>/', views.refuser_reservation, name='refuser_reservation'),
    path('gestionnaire_parc_profile/reservation/<int:reservation_id>/', views.details_reservation, name='details_reservation'),
    path('gestionnaire_parc_profile/confirmation_validation/', views.confirmation_validation, name='confirmation_validation'),
    
     path('gestionnaire_parc_profile/gerer_reservations_accepter/', views.gerer_reservations_accepter, name='gerer_reservations_accepter'),
     path('gestionnaire_parc_profile/refuser_reservation/<int:reservation_id>/', views.refuser_reservation, name='refuser_reservation'),
     
      path('gestionnaire_parc_profile/gerer_reservations_refuse/', views.gerer_reservations_refuse, name='gerer_reservations_refuse'),
    # Autres chemins URL pour d'autres vues

    
    path('creer_itineraire/', views.creer_itineraire, name='creer_itineraire'),
    path('modifier_itineraire/<int:itineraire_id>/', views.modifier_itineraire, name='modifier_itineraire'),
    path('supprimer_itineraire/<int:itineraire_id>/', views.supprimer_itineraire, name='supprimer_itineraire'),
    path('liste_itineraires/', views.liste_itineraires, name='liste_itineraires'),

  
    # Vues liées aux données de consommation de carburant
    path('gestionnaire_parc_profile/enregistrer_donnees_consommation/', views.enregistrer_donnees_consommation, name='enregistrer_donnees_consommation'),
    # path('modifier_donnees_consommation/<int:données_consommation_id>/', views.modifier_données_consommation, name='modifier_donnees_consommation'),
    # path('supprimer_donnees_consommation/<int:donnees_consommation_id>/', views.supprimer_donnees_consommation, name='supprimer_donnees_consommation'),
    path('gestionnaire_parc_profile/liste_donnees_consommation_carburant/', views.liste_donnees_consommation_carburant, name='liste_donnees_consommation_carburant'),
    path('gestionnaire_parc_profile/suivi_consommation/', views.suivi_consommation, name='suivi_consommation'),
    
    # Vues liées aux coûts
    path('enregistrer_cout/', views.enregistrer_cout, name='enregistrer_cout'),
    path('modifier_cout/<int:cout_id>/', views.modifier_cout, name='modifier_cout'),
    path('supprimer_cout/<int:cout_id>/', views.supprimer_cout, name='supprimer_cout'),
    path('liste_couts/', views.liste_couts, name='liste_couts'),

    # Vues liées aux notifications
    path('creer_notification/', views.creer_notification, name='creer_notification'),
    path('modifier_notification/<int:notification_id>/', views.modifier_notification, name='modifier_notification'),
    path('supprimer_notification/<int:notification_id>/', views.supprimer_notification, name='supprimer_notification'),
    path('liste_notifications/', views.liste_notifications, name='liste_notifications'),
    
      # Vues liées aux assurances
    path('ajouter_assurance/<int:vehicule_id>/', views.ajouter_assurance, name='ajouter_assurance'),
    path('mettre_a_jour_statut_vehicules/', views.mettre_a_jour_statut_vehicules, name='mettre_a_jour_statut_vehicules'),
    path('liste_assurances/', views.liste_assurances, name= 'liste_assurances'),

    #Vue pour la maintenance
     path('gestionnaire_intervention_profile/ajouter_maintenance/', views.ajouter_maintenance, name='ajouter_maintenance'),
     path('gestionnaire_intervention_profile/liste_maintenance/', views.liste_maintenance, name='liste_maintenance'),
      path('modifier_maintenance/<int:maintenance_id>/', views.modifier_maintenance, name='modifier_maintenance'),
    path('supprimer_maintenance/<int:maintenance_id>/', views.supprimer_maintenance, name='supprimer_maintenance'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)