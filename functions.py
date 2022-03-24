from ast import Return
from audioop import avg
from bdb import set_trace
from urllib import response
from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import ipdb
from datetime import datetime

load_dotenv()

#Read .env variable
API_key = os.getenv('API_key')

def getGeo(city_name):

    responseGeo = requests.get(url=f'http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=5&appid={API_key}')
    dataGeo = responseGeo.json()
    geo = dataGeo[0]
    getGeo.lat = geo.get("lat")
    getGeo.lon = geo.get("lon")
    #ipdb.set_trace()
    #geoPair = {"lat": lon, "lon": lon}
    #return lat, lon

def getTemperature(city_name):
    
    getGeo(city_name)
    lat = getGeo.lat
    lon = getGeo.lon
    #ipdb.set_trace()
    responseCity = requests.get(url=f'http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&units=metric&appid={API_key}')
    dataCity = responseCity.json()
    city = dataCity
    maxTemp = city.get("main").get("temp_max")
    minTemp = city.get("main").get("temp_min")
    avgTemp = city.get("main").get("temp")
    feels_likeTemp = city.get("main").get("feels_like")
    cityName = city.get("name")
    cityCountry = city.get("sys").get("country")
    dataMapping = {"max": maxTemp, "min": minTemp, "avg": avgTemp, "feels_like": feels_likeTemp, "city.name": cityName, "city.country": cityCountry, "time": datetime.utcnow()}
    return dataMapping