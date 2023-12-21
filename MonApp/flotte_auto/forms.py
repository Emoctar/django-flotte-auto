from django import forms
from django.forms import inlineformset_factory
from django.core.exceptions import ValidationError


from .models import *

# forms.py






# class DonnéesConsommationCarburantForm(forms.ModelForm):
#     class Meta:
#         model = DonnéesConsommationCarburant
#         fields = '__all__'  # Vous pouvez personnaliser les champs ici si nécessaire



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
    
    vehicule = forms.ModelChoiceField(queryset=Vehicule.objects.all(), empty_label="Sélectionnez un véhicule")





class ReservationVoitureForm(forms.ModelForm):
    vehicules = forms.ModelMultipleChoiceField(
        queryset=Vehicule.objects.filter(statut='Disponible'),
        widget=forms.SelectMultiple(attrs={'class': 'select2', 'data-placeholder': 'Sélectionnez les véhicules'}),
    )
    
    class Meta:
        model = ReservationVoiture
        fields = ['date_debut', 'date_fin', 'destination', 'motif', 'vehicules']

    def clean_vehicules(self):
        vehicules = self.cleaned_data.get('vehicules')

        # Assurez-vous que l'employé ne sélectionne pas plus de 3 véhicules
        if len(vehicules) > 3:
            raise forms.ValidationError("Vous ne pouvez sélectionner que 3 véhicules au maximum.")

        return vehicules

# class EmployeForm(forms.ModelForm):
#     class Meta:
#         model = Employé
#         fields = '__all__'
#     photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))


# class GestionnaireParcForm(forms.ModelForm):
#     class Meta:
#         model = GestionnaireParc
#         fields = '__all__'
#     photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))
    

# class GestionnaireInterventionForm(forms.ModelForm):
#     class Meta:
#         model = GestionnaireIntervention
#         fields = '__all__'
#     photo = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'form-control-file'}))    
        


class GestionnaireConsommationForm(forms.ModelForm):
    class Meta:
        model = GestionnaireConsommation
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
        fields =  '__all__'
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





class SearchForm(forms.Form):
    start_date = forms.DateField(label='Date de début')
    end_date = forms.DateField(label='Date de fin')
    vehicle = forms.ModelChoiceField(queryset=Vehicule.objects.all(), required=False, label='Véhicule')
    
    
class ConsommationCarburantForm(forms.ModelForm):
    class Meta:
        model = ConsommationCarburant
        fields = ['vehicule', 'date', 'quantite_carburant', 'distance_parcourue']
        widgets = {
            'reservation': forms.HiddenInput(),
        }
        
        



class PanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = '__all__'
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'commentaire': forms.Textarea(attrs={'rows': 4}),
            'type_panne': forms.Select(choices=Panne.TYPE_PANNE_CHOICES),
        }

