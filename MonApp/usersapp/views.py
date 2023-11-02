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
        elif self.request.user.groups.filter(name='Gestionnaire Consommation').exists():
            return reverse_lazy('gestionnaire_consommation_profile')
        elif self.request.user.groups.filter(name='Employe').exists():
            return reverse_lazy('employe_profile')
        elif self.request.user.groups.filter(name='Gestionnaire Intervention').exists():
            return reverse_lazy('gestionnaire_intervention_profile')
        else:
            # Redirection par défaut pour les autres utilisateurs (vous pouvez personnaliser)
            return reverse_lazy('home')  # Redirigez vers la page d'accueil par défaut
        
from django.contrib.auth.views import PasswordResetDoneView

class CustomPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/mypassword_reset_done.html' 
    

from django.contrib.auth.views import PasswordResetConfirmView

class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    template_name = 'registration/password_reset_confirm.html'  # Spécifiez le modèle personnalisé ici
    success_url = reverse_lazy('login')  #
    

from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required  # Utilisez cette décoration pour protéger l'accès aux pages de profil
def gestionnaire_parc_profile(request):
    context = {
        'user': request.user  # Transmettez l'utilisateur connecté au modèle
    }
    # Logique spécifique au profil gestionnaire_parc
    return render(request, 'GesParc/Dashbord.html')

@login_required
def gestionnaire_consommation_profile(request):
    # Logique spécifique au profil gestionnaire_consommation
    return render(request, 'GesConsommation/profile.html')

@login_required
def employe_profile(request):
    # Logique spécifique au profil employe
    return render(request, 'Employe/profile.html')

@login_required
def gestionnaire_intervention_profile(request):
    # Logique spécifique au profil gestionnaire_intervention
    return render(request, 'GesIntervention/profile.html')

# class CustomLogoutView(LogoutView):
#     # Vous pouvez personnaliser la vue de déconnexion ici si nécessaire
#     pass





