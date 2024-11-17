from django.urls import path
from . import views

urlpatterns = [
    path('', views.question, name = 'question'),
    path('home', views.home, name = 'home'),
    path('details/<int:id>', views.details, name = 'details'), 
    path('int:Question_id/', views.vote, name='vote'),  
    path('<int:question_id>/choice', views.choice, name = 'choice'),
]

