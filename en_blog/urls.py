from django.urls import path
from . import views

app_name = 'en_blog'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.single_post, name='single_post')
]