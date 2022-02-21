from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def display(request):
    country_code = request.POST['country']
    state = request.POST['place']
    response = requests.get(f"http://api.weatherapi.com/v1/current.json?key=ba4d571b2ef94267b10122724212307&q={state}")
    if(response.status_code == 200):
        weatherdata = response.json()
        #weathericon = response1.json()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        
    else:
        return HttpResponse('<h1>Data Unavailable</h1>')
    
    return render(request, 'display.html', {
        
        'temp' : weatherdata['current']['temp_c'],
        'icon' : weatherdata['current']['condition']['icon'],
        'condition' : weatherdata['current']['condition']['text'],
        'state' : state,
        'time' : current_time,
        'wind_speed' : weatherdata['current']['wind_kph'],
        'humidity' : weatherdata['current']['humidity'],
        'uv' : weatherdata['current']['uv'],
    })