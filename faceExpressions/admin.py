from django.contrib import admin
from .models import Candidats, Postes
  
class CandidatAdmin(admin.ModelAdmin):
    list_display =  ["first_name", "last_name", "email","photo_file_name","video_file_name", "poste", 'happy', 'disgust', 'fear', 'angry',"surprise", 'sad', "naturel"]

admin.site.register(Candidats, CandidatAdmin)

class PosteAdmin(admin.ModelAdmin):
    list_display =  ["poste_type"]

admin.site.register(Postes, PosteAdmin)