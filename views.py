from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def home(request):
  return render(request, 'index.html')

def get_weather_from_ip(request):
  print(request.GET.get("ip_address"))
  data = {"weather_data": 20}
  return JsonResponse(data)

import requests
def get_location_from_ip(ip_address):
    response = requests.get("http://ip-api.com/json/{}".format(ip_address))
    return response.json()

def get_weather_from_ip(request):
  ip_address = request.GET.get("ip")
  location = get_location_from_ip(ip_address)
  city = location.get("city")
  country_code = location.get("countryCode")
  s = "You're in {}, {}".format(city, country_code)
  data = {"weather_data": s}
  return JsonResponse(data)