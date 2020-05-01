from django.urls import path
from . import views

app_name = 'en_app'

urlpatterns = [
    path('', views.home, name='home'),
]