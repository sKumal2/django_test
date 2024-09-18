#creating my first urls
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('contact/', views.contact),
    path('resume/', views.resume),
]

