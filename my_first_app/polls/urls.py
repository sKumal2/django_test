#creating my first urls
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name= "index"),
    path('home/', views.home),
    path('contact/', views.contact),
]

