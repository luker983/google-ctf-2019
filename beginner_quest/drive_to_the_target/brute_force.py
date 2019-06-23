import requests
from requests_html import HTMLSession

URL = 'https://drivetothetarget.web.ctfcompetition.com'

TOKEN = None
LAT = None
LON = None

#while True:
#    get_coords()
#    move()
session = HTMLSession()

def get_coords():
    r = session.get(url=URL)
    inputs = r.html.find('input')
    lat = inputs[0].attrs.get('value')
    lon = inputs[1].attrs.get('value')
    token = inputs[2].attrs.get('value')
    return (lat, lon, token)

def move():
    
#PARAMS = {'lat': 0.0, 'lon': 0.0, 'token': TOKEN} 
#r = session.get(url=URL, params=PARAMS)

(LAT, LON, TOKEN) = get_coords()
