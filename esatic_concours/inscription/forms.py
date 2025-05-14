from django import forms
from .models import  Inscription

class InscriptionForm(forms.ModelForm):

    class Meta:
        model = Inscription
        fields = ['nom', 'prenom', 'niveauEtude','email', 'etablissementOrigine', 'concoursSouhaiter', 'extraitNaissance', 'certificatNationalite', 'lettreMotivation', 'diplome', 'photo']
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'input'}),
            'prenom': forms.TextInput(attrs={'class': 'input'}),
            'niveauEtude': forms.TextInput(attrs={'class': 'input'}),
            'email': forms.EmailInput(attrs={'class': 'input'}),
            'etablissementOrigine': forms.TextInput(attrs={'class': 'input'}),
            'extraitNaissance': forms.FileInput(attrs={'class': 'file-input'}),
            'certificatNationalite': forms.FileInput(attrs={'class': 'file-input'}),
            'lettreMotivation': forms.FileInput(attrs={'class': 'file-input'}),
            'diplome': forms.FileInput(attrs={'class': 'file-input'}),
            'photo': forms.FileInput(attrs={'class': 'file-input'}),
        }