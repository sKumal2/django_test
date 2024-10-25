from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name = 'question'),
    path('home', views.home, name = 'home'),
    path('details/<int:id>', views.details, name = 'details'), 
    path('int:Question_id/', views.vote, name='vote'),  
    path('vote', views.vote, name='vote'),  
    path('master', views.master, name='master'),   
    path('que', views.question, name='question'),
    path('choice/<int:id>', views.choice, name = 'choice'),
]