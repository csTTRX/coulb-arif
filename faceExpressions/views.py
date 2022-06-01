from django.shortcuts import redirect, render
from faceExpressions.models import Candidats
from .forms import Candidat_form
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,"home.html", context={})

def upload_candature(request):
    form = Candidat_form()

    if request.method == "POST":
        form = Candidat_form(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
    return render(request, "upload_candidature.html", context= {"form":form})

@login_required
def admin_dash(request):
    candidats = Candidats.objects.all()
    totals = len(candidats)
    return render(request, 'admin_dash.html', context = {"candidats":candidats, 'totals': totals})
    