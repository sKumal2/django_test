from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('details/<int:id>', views.details, name = 'details'),
    path('<int:Question_id>/', views.details, name = 'details'),
    path("<int:Question_id>/", views.results, name="results"),
    path("<int:Question_id>/", views.vote, name= "vote"),
    path('form', views.home, name= 'form'),
]