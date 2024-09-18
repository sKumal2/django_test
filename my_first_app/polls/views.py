from django.shortcuts import render

# Create your views here.
#writing my first view
from django.http import HttpResponse
from django.template import loader

def index(request):
    return HttpResponse("Hello World! You're at the polls index.")

def members(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())
