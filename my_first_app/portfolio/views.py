from django.shortcuts import render

# Create your views here.
#writing my first view
from django.http import HttpResponse
from django.template import loader

def home(request):
    home = loader.get_template('home.html')
    return HttpResponse(home.render())

def contact(request):
    contact = loader.get_template('contact.html')
    return HttpResponse(contact.render())

def resume(request):
    resume = loader.get_template('resume.html')
    return HttpResponse(resume.render())

def projects(request):
    projects = loader.get_template('projects.html')
    return HttpResponse(projects.render())
