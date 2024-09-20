from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Polls

# Create your views here.
def home(request):
    home = loader.get_template('index.html')
    member = Polls.objects.all().values()
    index = {
        'home' : member,
    }
    return HttpResponse(home.render(index, request))