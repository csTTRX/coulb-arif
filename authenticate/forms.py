from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
class register_form(UserCreationForm):
    
    
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'r_input' , 'placeholder':'Email'}))
    first_name = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class':'r_input' , 'placeholder':'Prénom'}))
    last_name = forms.CharField(max_length=255 ,widget=forms.TextInput(attrs={'class':'r_input' , 'placeholder':'Nom'}))

    class Meta:

        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

    def __init__(self, *args, **kwargs):

        super(register_form, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs= {"class" :"r_input" , "placeholder":"Nom d'utilisateur"}
        self.fields['password1'].widget.attrs= {"class" :"r_password" , "placeholder":"Password"}
        self.fields['password2'].widget.attrs= {"class" :"r_password" , "placeholder":"Confirmez le password"}

class LoginForm(forms.Form):

    username = forms.CharField(widget=forms.TextInput(attrs={'class':'r_input' , 'placeholder':"Nom d'utilisateur"}))
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class':'r_password' , 'placeholder':'password'}))