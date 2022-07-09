from django.shortcuts import render
import requests

# Create your views here.

def home(request):
    response = requests.get("https://restcountries.com/v3.1/all", verify=False).json
    return render(request, 'home.html', {'response': response})
