from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

# Dans votre fichier urls.py






# Remplacez 'myapp' par le nom de votre application

urlpatterns = [
  
   
  
   path('gestionnaire_parc_profile/votre_vue/', views.votre_vue, name='votre_vue'),
    # Ajoutez d'autres URL au besoin
   
 
    
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
    path('employe_profile/historique_reservations/', views.historique_reservations, name='historique_reservations'),
    path('employe_profile/creer_reservation/', views.creer_reservation, name='creer_reservation'),
    path('employe_profile/modifier_reservation/<int:reservation_id>/', views.modifier_reservation, name='modifier_reservation'),
    path('employe_profile/annuler_reservation/<int:reservation_id>/', views.annuler_reservation, name='annuler_reservation'),
    path('gerer_reservations_attente/supprimer_reservation/<int:reservation_id>/', views.supprimer_reservation, name='supprimer_reservation'),
    path('gestionnaire_parc_profile/liste_toutes_reservations/', views.liste_toutes_reservations, name='liste_toutes_reservations'),

    
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
      
   
    # Vues liées aux données de consommation de carburant
      path('enregistrer_donnees_consommation/<int:reservation_id>/', views.enregistrer_donnees_consommation, name='enregistrer_donnees_consommation'),
    # path('modifier_donnees_consommation/<int:données_consommation_id>/', views.modifier_données_consommation, name='modifier_donnees_consommation'),
    # path('supprimer_donnees_consommation/<int:donnees_consommation_id>/', views.supprimer_donnees_consommation, name='supprimer_donnees_consommation'),
    path('gestionnaire_parc_profile/liste_donnees_consommation_carburant/', views.liste_donnees_consommation_carburant, name='liste_donnees_consommation_carburant'),
    path('gestionnaire_parc_profile/suivi_consommation/', views.suivi_consommation, name='suivi_consommation'),
    
    # Vues liées aux coûts
    path('enregistrer_cout/', views.enregistrer_cout, name='enregistrer_cout'),
    path('modifier_cout/<int:cout_id>/', views.modifier_cout, name='modifier_cout'),
    path('supprimer_cout/<int:cout_id>/', views.supprimer_cout, name='supprimer_cout'),
    path('liste_couts/', views.liste_couts, name='liste_couts'),

 
      # Vues liées aux assurances
    path('gestionnaire_parc_profile/ajouter_assurance/', views.ajouter_assurance, name='ajouter_assurance'),
    path('gestionnaire_parc_profile/mettre_a_jour_statut_vehicules/', views.mettre_a_jour_statut_vehicules, name='mettre_a_jour_statut_vehicules'),
    path('gestionnaire_parc_profile/liste_assurances/', views.liste_assurances, name= 'liste_assurances'),
    path('gestionnaire_parc_profile/modifier_assurance/<int:assurance_id>/', views.modifier_assurance, name='modifier_assurance'),

    #Vue pour la maintenance
     path('gestionnaire_intervention_profile/ajouter_maintenance/', views.ajouter_maintenance, name='ajouter_maintenance'),
     path('gestionnaire_intervention_profile/liste_maintenance/', views.liste_maintenance, name='liste_maintenance'),
      path('gestionnaire_intervention_profile/modifier_maintenance/<int:maintenance_id>/', views.modifier_maintenance, name='modifier_maintenance'),
    path('supprimer_maintenance/<int:maintenance_id>/', views.supprimer_maintenance, name='supprimer_maintenance'),
     path('gestionnaire_intervention_profile/terminer_maintenance/<int:maintenance_id>/', views.terminer_maintenance, name='terminer_maintenance'),
      path('gestionnaire_parc_profile/terminer_reservation/<int:reservation_id>/', views.terminer_reservation, name='terminer_reservation'),
      
      
    #PANNE
    
    path('gestionnaire_intervention_profile/creer_panne/', views.creer_panne, name='creer_panne'),
    path('gestionnaire_intervention_profile/modifier_panne/<int:panne_id>/', views.modifier_panne, name='modifier_panne'),
    path('gestionnaire_intervention_profile/supprimer_panne/<int:panne_id>/', views.supprimer_panne, name='supprimer_panne'),
    path('gestionnaire_intervention_profile/liste_pannes/', views.liste_pannes, name='liste_pannes'),

      

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



