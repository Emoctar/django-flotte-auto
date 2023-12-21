from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegistrationForm(UserCreationForm):
	first_name = forms.CharField(label='Prénom')
	last_name = forms.CharField(label='Nom')
	email = forms.EmailField(label='Adresse e-mail')
	class Meta(UserCreationForm.Meta):
		model = User
		fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email')
  
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        # Supprimez les champs inutiles
        for field_name in ['password', 'username']:
            del self.fields[field_name]
 
  
# forms.py
# # forms.py
# from django import forms
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User
# from flotte_auto.models import Employé, GestionnaireParc, GestionnaireIntervention

# class UserProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']

# class EmployeeProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = Employé
#         fields =  ['telephone', 'adresse', 'photo']

# class ManagerProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = GestionnaireParc
#         fields = ['telephone', 'adresse', 'photo']

# class InterventionManagerProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = GestionnaireIntervention
#         fields = ['telephone', 'adresse', 'photo']


# # forms.py
# from django import forms
# from django.contrib.auth.forms import UserChangeForm
# from django.contrib.auth.models import User
# from flotte_auto.models import Employé, GestionnaireParc, GestionnaireIntervention

# class UserProfileForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'email']

# class EmployeeProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = Employé
#         fields = ['telephone', 'adresse', 'photo']

#     def __init__(self, *args, **kwargs):
#         user_instance = kwargs.pop('user_instance', None)
#         super(EmployeeProfileForm, self).__init__(*args, **kwargs)

#         # Ajouter des champs de modèle User au formulaire
#         if user_instance:
#             self.fields['first_name'] = forms.CharField(max_length=30, initial=user_instance.employé.utilisateur.first_name)
#             self.fields['last_name'] = forms.CharField(max_length=30, initial=user_instance.employé.utilisateur.last_name)
#             self.fields['email'] = forms.EmailField(initial=user_instance.employé.utilisateur.email)
            
            
# class ManagerProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)

#     class Meta:
#         model = GestionnaireParc
#         fields =  ['telephone', 'adresse', 'photo']

#     def __init__(self, *args, **kwargs):
#         user_instance = kwargs.pop('user_instance', None)
#         super(ManagerProfileForm, self).__init__(*args, **kwargs)

#         # Ajouter des champs de modèle User au formulaire
#         if user_instance:
#             self.fields['Prenom'] = forms.CharField(max_length=30, initial=user_instance.gestionnaireparc.utilisateur.first_name)
#             self.fields['Nom'] = forms.CharField(max_length=30, initial=user_instance.gestionnaireparc.utilisateur.last_name)
#             self.fields['mail'] = forms.EmailField(initial=user_instance.gestionnaireparc.utilisateur.email)

# class InterventionManagerProfileForm(forms.ModelForm):
#     telephone = forms.CharField(max_length=15, required=False)
#     adresse = forms.CharField(max_length=255, required=False)
#     photo = forms.ImageField(required=False)
    
#     class Meta:
#         model = GestionnaireIntervention
#         fields =  ['telephone', 'adresse', 'photo']

#     def __init__(self, *args, **kwargs):
#         user_instance = kwargs.pop('user_instance', None)
#         super(InterventionManagerProfileForm, self).__init__(*args, **kwargs)

#         # Ajouter des champs de modèle User au formulaire
#         if user_instance:
#             self.fields['first_name'] = forms.CharField(max_length=30, initial=user_instance.gestionnaireintervention.utilisateur.first_name)
#             self.fields['last_name'] = forms.CharField(max_length=30, initial=user_instance.gestionnaireintervention.last_name)
#             self.fields['email'] = forms.EmailField(initial=user_instance.gestionnaireintervention.utilisateur.email)
            
            
            
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User

class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserProfileUpdateForm, self).__init__(*args, **kwargs)
        # Supprimez les champs inutiles
        for field_name in ['password']:
            del self.fields[field_name]



# forms.py

from django import forms
from django.contrib.auth.forms import UserChangeForm
from flotte_auto.models import GestionnaireParc, Employé, GestionnaireIntervention
from django.contrib.auth import get_user_model

class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
class UserProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

class GestionnaireParcForm(forms.ModelForm):
    class Meta:
        model = GestionnaireParc
        fields = ['telephone', 'adresse', 'photo']
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
class EmployeForm(forms.ModelForm):
    class Meta:
        model = Employé
        fields = ['telephone', 'adresse', 'photo']
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
class GestionnaireInterventionForm(forms.ModelForm):
    class Meta:
        model = GestionnaireIntervention
        fields = ['telephone', 'adresse', 'photo']
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))