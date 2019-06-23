import requests
from requests_html import HTMLSession
import time

URL = 'https://drivetothetarget.web.ctfcompetition.com'
LATSTEP = -0.0001
LONSTEP = -0.000175

FINLAT=51.4921
FINLON=-0.1933
#while True:
#    get_coords()
#    move()
session = HTMLSession()

def get_coords():
    r = session.get(url=URL)
    inputs = r.html.find('input')
    lat = float(inputs[0].attrs.get('value'))
    lon = float(inputs[1].attrs.get('value'))
    token = inputs[2].attrs.get('value')
    return (lat, lon, token)
    

(lat, lon, token) = get_coords()

i = 0
while True:
    if i > 3:
        break

    if lat < FINLAT:
        LATSTEP = 0
    if lon < FINLON:
        LONSTEP = 0

    #print('moving from', str(lat), str(lon), 'to', str(lat + STEP), str(lon))
    params = {'lat': lat+LATSTEP, 'lon': lon+LONSTEP, 'token': token} 
    r = session.get(url=URL, params=params)

    inputs = r.html.find('input')
    lat = float(inputs[0].attrs.get('value'))
    lon = float(inputs[1].attrs.get('value'))
    token = inputs[2].attrs.get('value')

    #print(r.html.text)
    if r.html.search('closer'):
        print('getting closer:', str(lat), str(lon))
        continue
    elif r.html.search('away'):
        i += 1
        print('reversing direction for lon')
'''
# Change LON
i = 0
while True:
    if i > 3:
        break
    #print('moving from', str(lat), str(lon), 'to', str(lat + STEP), str(lon))
    params = {'lat': lat, 'lon': lon+LONSTEP, 'token': token} 
    r = session.get(url=URL, params=params)


    inputs = r.html.find('input')
    lat = float(inputs[0].attrs.get('value'))
    lon = float(inputs[1].attrs.get('value'))
    token = inputs[2].attrs.get('value')

    #print(r.html.text)
    if r.html.search('closer'):
        print('getting closer:', str(lat), str(lon))
        continue
    elif r.html.search('away'):
        i += 1
        print('reversing direction for lon')
        STEP = -LATSTEP
    #time.sleep(3)

# Change LAT
i = 0
while True:
    if i > 3:
        break
    #print('moving from', str(lat), str(lon), 'to', str(lat + STEP), str(lon))
    params = {'lat': lat+LATSTEP, 'lon': lon, 'token': token} 
    r = session.get(url=URL, params=params)


    inputs = r.html.find('input')
    lat = float(inputs[0].attrs.get('value'))
    lon = float(inputs[1].attrs.get('value'))
    token = inputs[2].attrs.get('value')

    #print(r.html.text)
    if r.html.search('closer'):
        print('getting closer:', str(lat), str(lon))
        continue
    elif r.html.search('away'):
        i += 1
        print('reversing direction for lat')
        STEP = -LONSTEP
    #time.sleep(3)
'''
print('Latitude:', str(lat), 'Longitude:', str(lon), 'Token:', token)


while True:
    time.sleep(1)

