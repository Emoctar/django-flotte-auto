from django.urls import path, include
from django.contrib.auth import views as auth_views
from usersapp import views

urlpatterns =[
	
	#path('accounts/', include('django.contrib.auth.urls')),
	# path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),	
  path('login/', views.CustomLoginView.as_view(), name='login'),  # Utilisez votre vue de connexion personnalisée
	path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
	path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name = 'password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='registration/mypassword_reset_done.html'), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('register/', views.register, name = 'register'),
    
     path('gestionnaire_parc_profile/', views.gestionnaire_parc_profile, name='gestionnaire_parc_profile'),
    
    path('employe_profile/', views.employe_profile, name='employe_profile'),
    path('gestionnaire_intervention_profile/', views.gestionnaire_intervention_profile, name='gestionnaire_intervention_profile'),
    
    path('update_profile/', views.update_profile, name='update_profile'),
    
    
    # path('view_profile/', views.view_profile, name='view_profile'),
    # path('edit_profile/', views.UserProfileUpdateView.as_view(), name='edit_profile'),
    #  path('edit_profile/parc/', views.GestionnaireParcUpdateView.as_view(), name='edit_gestionnaire_parc_profile'),
    # path('edit_profile/intervention/',views. GestionnaireInterventionUpdateView.as_view(), name='edit_gestionnaire_intervention_profile'),
]


