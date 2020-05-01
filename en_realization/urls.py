from django.urls import path
from . import views

app_name = 'en_realization'

urlpatterns = [
    path('', views.home, name='home'),
    path('<slug:slug>/', views.realization, name='realization'),
]