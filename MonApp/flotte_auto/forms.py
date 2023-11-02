from django import forms
from django.forms import inlineformset_factory


from .models import *


class DonnéesConsommationCarburantForm(forms.ModelForm):
    class Meta:
        model = DonnéesConsommationCarburant
        fields = '__all__'  # Vous pouvez personnaliser les champs ici si nécessaire



class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'  # Vous pouvez personnaliser les champs ici si nécessaire




class CoutForm(forms.ModelForm):
    class Meta:
        model = Cout
        fields = '__all__'  # Vous pouvez personnaliser les champs ici si nécessaire



class ItineraireForm(forms.ModelForm):
    class Meta:
        model = Itineraire
        fields = '__all__'


class MaintenanceForm(forms.ModelForm):
    class Meta:
        model = Maintenance
        fields = ['vehicule', 'date_maintenance', 'description', 'cout']
    
    vehicule = forms.ModelChoiceField(queryset=Vehicule.vehicules_disponibles(), empty_label="Sélectionnez un véhicule")




class ReservationVoitureForm(forms.ModelForm):
    vehicules = forms.ModelMultipleChoiceField(
        queryset=Vehicule.objects.all(),
        widget=forms.SelectMultiple(attrs={'class': 'form-control'}),
    )

    class Meta:
        model = ReservationVoiture
        fields = ['date_debut', 'date_fin', 'destination', 'motif', 'vehicules']

   




class GestionnaireParcForm(forms.ModelForm):
    class Meta:
        model = GestionnaireParc
        fields = '__all__'
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
    

class GestionnaireConsommationForm(forms.ModelForm):
    class Meta:
        model = GestionnaireConsommation
        fields = '__all__'
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    
class GestionnaireInterventionForm(forms.ModelForm):
    class Meta:
        model = GestionnaireIntervention
        fields = '__all__'
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))    
        
        
class ConducteurForm(forms.ModelForm):
    class Meta:
        model = Conducteur
        fields = '__all__'
    photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
        

class VehiculeForm(forms.ModelForm):
    class Meta:
        model = Vehicule
        fields = '__all__'
        photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
        
        


class NoteConducteurForm(forms.ModelForm):
    class Meta:
        model = PerformanceConduite
        fields = ['note', 'commentaire']
        
        


class AssuranceForm(forms.ModelForm):
    class Meta:
        model = Assurance
        fields = ['compagnie_assurance', 'numero_police', 'date_debut', 'date_fin', 'prime_annuelle']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Vous pouvez ajouter des attributs HTML personnalisés ici si nécessaire
