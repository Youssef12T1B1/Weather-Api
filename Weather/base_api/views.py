from importlib.metadata import requires
from urllib import response
from urllib.request import Request
from django.shortcuts import redirect, render
import requests



async def home(request):
    api = 'http://api.openweathermap.org./data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q='
    city = 'morocco'
    if request.method == 'POST':
        if request.POST.get('q'):
            city = request.POST.get('q')
        else:
            return redirect('home')

       
    url = api +  city
    response = requests.get(url)
    content = response.json()

   
    

    weather = {
        'city': city,
        'description': content['weather'][0]['description'],
        'temprature': content['main']['temp'],
        'humidity': content['main']['humidity'],
        'wind': content['wind']['speed'],
        'icon': content['weather'][0]['icon'],
        
        
    }
    return render(request, 'home.html', weather)    
    


    

  
