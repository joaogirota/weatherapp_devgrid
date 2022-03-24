from ast import Return
from audioop import avg
from bdb import set_trace
from email.policy import default
from urllib import response
from webbrowser import get
from flask import Flask, jsonify
import os
from dotenv import load_dotenv
import requests
import json
import pandas as pd
import ipdb
from functions import getGeo, getTemperature
from flask_caching import Cache
import json


load_dotenv()
cache_ttl = os.getenv('cache_ttl')
default_max_number = os.getenv('default_max_number')


#Simple cache config
config = {
    "DEBUG": True,
    "CACHE_TYPE": "SimpleCache",  # caching type
    "CACHE_DEFAULT_TIMEOUT": 300 # default Cache Timeout
}


app = Flask(__name__)

app.config.from_mapping(config)
cache = Cache(app)

@app.route('/temperature/<string:city_name>', methods=['GET'])
@cache.cached(timeout=int(cache_ttl))
def runTemp(city_name):

   
    return getTemperature(city_name)

@app.route('/cache', methods=['GET'])
def runCache():
    cacheSize = len(cache.cache._cache)
    return str(cacheSize)
cache.clear()

@app.route('/temperature', methods=['GET'])
def allCities():
    new_dict = {}
    x = cache.cache._cache.decode("utf-8")
    #x = x.decode("utf-8")
    #y = list(cache.cache._cache.items())
    #y = str(y, "utf-8")
    a = json.dumps(x)
    a = json.loads(a)

    #y = json.loads(x.encode('utf-8'))
    #for key, value in x:
        #new_dict[key] = 
    return x


    """ decoded = {}
    for key, value in cache.cache._cache.items():
        #decoded[key.decode("utf-8")] = value.decode("utf-8") """
   
        #return str(value)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
#ipdb.set_trace()