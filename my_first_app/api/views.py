from django.shortcuts import render
from .forms import CityForm
import requests

# Create your views here.
def get_weather(request):
    # api_key = 'https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m'
