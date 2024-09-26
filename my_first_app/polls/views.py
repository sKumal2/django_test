from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Polls

# Create your views here.
def home(request):
    home = loader.get_template('index.html')
    member = Polls.objects.all().values()
    context = {
        'home' : member,
    }
    return HttpResponse(home.render(context, request))

def details(request, id):
    template = loader.get_template('details.html')
    details = Polls.objects.get(id=id)
    context = {
        'details' : details
    }
    return HttpResponse(template.render(context, request))
