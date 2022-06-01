from re import template
from django.urls import path

from authenticate.views import register, login_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
urlpatterns = [
    path("register/", register, name="register"),
    path('login/', login_view, name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]

urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)