from unicodedata import name
from django.urls import path
from .views import *
urlpatterns = [
    path("", home, name = "home" ),
    # path("streaming/", streaming, name = "streaming" ),
    # path('video_feed/', video_feed, name='video_feed'),
    path('upload_candature/', upload_candature, name = 'candidature'),
    path('admin_dash', admin_dash, name = 'admin_dash')
]
