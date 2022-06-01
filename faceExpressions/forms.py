from django import forms
from .models import Candidats
class Candidat_form(forms.ModelForm):

    first_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Prénom"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Nom"}))
    adress = forms.CharField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Adress"}))
    email = forms.EmailField(widget=forms.TextInput(attrs={"class":"form_input", "placeholder":"Email"}))
    photo_file_name = forms.ImageField(widget=forms.FileInput(attrs={"class":"img_input"}))
    cv_file_name = forms.FileField(widget=forms.FileInput(attrs={"class":"img_input"}))
    video_file_name = forms.FileField(widget=forms.FileInput(attrs={"class":"img_input"}))
    
    class Meta:
        model = Candidats
        fields = ['first_name', 'last_name','adress','email', 'photo_file_name','cv_file_name','video_file_name', 'poste']