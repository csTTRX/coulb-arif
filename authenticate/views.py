from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site 
from django.contrib.auth import login, authenticate
from .forms import *
# Create your views here.

def register(request):
    form = register_form()
    domain = get_current_site(request)
    if request.method =="POST":
        form = register_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            subject = 'zfer compte acctivation'
            to_mail = form.cleaned_data.get('email')
            message = render_to_string('acc_mail.html', {
                'user': request.user,
                'domain': domain,
                'uid' : urlsafe_base64_encode(force_bytes(request.user.pk))
            })
            email = EmailMessage(subject, message, 'contact@02xcode.com', to=[to_mail])
            email.send()
    return render(request, "register.html", context={'form':form})

def login_view(request):

    form = LoginForm()
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            user_authenticated = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )

            if user_authenticated  is not None and user_authenticated.is_active == True:
                login(request, user_authenticated )
                return redirect('home')
            else:
                HttpResponse("Votre compte n'est pas encore été activé, Veuillez confirmer votre adresse mail")
    return render(request, 'login.html' , context={'form':form,})