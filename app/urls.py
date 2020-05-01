from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('portale-internetowe/', views.portal, name='portal'),
    path('sklepy-internetowe/', views.shop, name='shop'),
    path('strony-wizytowki/', views.on_page_website, name='on_page_website'),
    path('e-marketing/', views.e_marketing, name='e_marketing'),
    path('kontakt/', views.contact, name='contact'),
    path('wycena-online/', views.valuation_online, name='valuation'),
    path('polityka-prywatnosci/', views.privacy_policy, name='privacy_policy'),
    path('opinie/', views.reviews, name='reviews'),
]