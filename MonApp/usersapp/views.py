from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from usersapp.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages

def register(request):
	if request.method == 'POST' :
		form = UserRegistrationForm(request.POST)
		if form.is_valid():
			form.save()		
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request,user)	
			messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')					
			return redirect('home')
	else :
		form = UserRegistrationForm()
	return render(request,'registration/register.html',{'form' : form})


########################################################################
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView

from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        # Déterminez ici le profil de l'utilisateur, par exemple en vérifiant ses groupes, attributs, etc.
        if self.request.user.groups.filter(name='Gestionnaire Parc').exists():
            return reverse_lazy('gestionnaire_parc_profile')
        elif self.request.user.groups.filter(name='Employe').exists():
            return reverse_lazy('update_profile')
        elif self.request.user.groups.filter(name='Gestionnaire Intervention').exists():
            return reverse_lazy('update_profile')
        else:
            # Redirection par défaut pour les autres utilisateurs 
            return reverse_lazy('home')  # Redirigez vers la page d'accueil par défaut
        
from django.contrib.auth.views import PasswordResetDoneView

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/mypassword_reset_done.html' 
    

from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/mypassword_reset_confirm.html'  # Spécifiez le modèle personnalisé ici
    success_url = reverse_lazy('login')  
    
from django.contrib.auth.views import PasswordResetView
class CustomPasswordResetView(PasswordResetView):
    template_name = 'registration/password_reset.html'
    success_url = reverse_lazy('mypassword_reset_done')
    
    

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .decorateurs import gestionnaire_parc_required, employe_required, gestionnaire_intervention_required
from .forms import *

@login_required
@gestionnaire_parc_required
def gestionnaire_parc_profile(request):
    context = {
        'user': request.user  # Transmettez l'utilisateur connecté au modèle
    }
    # Logique spécifique au profil gestionnaire_parc
    return render(request, 'GesParc/Dashbord.html')

@login_required
@employe_required
def employe_profile(request):
    # Logique spécifique au profil employe
    return render(request, 'Employe/edit_profile.html')

@login_required
@gestionnaire_intervention_required
def gestionnaire_intervention_profile(request):
    # Logique spécifique au profil gestionnaire_intervention
    return render(request, 'GesIntervention/edit_profile.html')




@login_required
def edit_profile(request):
    user = request.user
    template_name = 'base.html'  # Par défaut
    
    print(f"User Groups: {user.groups.all()}")  # Ajout de cette ligne pour vérifier les groupes de l'utilisateur

    if user.groups.filter(name='Gestionnaire Parc').exists():
        template_name = 'GesParc/home_GesParc.html'
    elif user.groups.filter(name='Employe').exists():
        template_name = 'Employe/home_emp.html'
    elif user.groups.filter(name='Gestionnaire Intervention').exists():
        template_name = 'GesIntervention/GesInterv_home.html'
        
    print(f"Selected Template: {template_name}")

    return render(request, template_name, {'user': user, 'template_name': template_name})



# views.py

# views.py
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.db import transaction
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import UserProfileUpdateForm, EmployeForm, GestionnaireParcForm, GestionnaireInterventionForm
from flotte_auto.models import Employé, GestionnaireParc, GestionnaireIntervention

@login_required
def update_profile(request):
    user = request.user
    profile_instance = None

    if user.groups.filter(name='Gestionnaire Parc').exists():
        profile_instance = user.gestionnaireparc
        form_class = GestionnaireParcForm
        template_name = 'GesParc/edit_profile.html'
    elif user.groups.filter(name='Gestionnaire Intervention').exists():
        profile_instance = user.gestionnaireintervention
        form_class = GestionnaireInterventionForm
        template_name = 'GesIntervention/edit_profile.html'
    elif user.groups.filter(name='Employe').exists():
        profile_instance = user.employé
        form_class = EmployeForm
        template_name = 'Employe/edit_profile.html'
    else:
        form_class = UserProfileUpdateForm

    if request.method == 'POST':
        form = form_class(request.POST, request.FILES, instance=profile_instance)
        password_form = PasswordChangeForm(request.user, request.POST)
        user_form = UserProfileUpdateForm(request.POST, instance=user)  # Utilisez UserProfileUpdateForm avec instance=user

        if form.is_valid() and password_form.is_valid() and user_form.is_valid():
            return form_valid(request, user_form, form, password_form)
        else:
            return form_invalid(request, form)
    else:
        form = form_class(instance=profile_instance)
        password_form = PasswordChangeForm(request.user)
        user_form = UserProfileUpdateForm(instance=user)  # Utilisez UserProfileUpdateForm ici

    return render(
        request,
        template_name,
        {'form': form, 'password_form': password_form, 'user_form': user_form}
    )

def form_valid(request, user_form, form, password_form):
    with transaction.atomic():
        user = request.user

        if password_form.cleaned_data.get('new_password1'):
            password_form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Mot de passe modifié avec succès.')

        if user_form.is_valid():
            user_form.save()

        if form.is_valid():
            form.save()

        messages.success(request, 'Profil mis à jour avec succès.')

    return redirect('login')

def form_invalid(request, form):
    messages.error(request, 'Erreur dans le formulaire.')
    return render(request, 'edit_profile.html', {'form': form})
