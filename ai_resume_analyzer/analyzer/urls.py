# analyzer/urls.py
from django.urls import path
from . import views

app_name = 'analyzer'  # Namespacing the app URLs

urlpatterns = [
    path('', views.upload_resume, name='upload_resume'),  # Home page
]