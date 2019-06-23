import requests
import lxml.html

URL = 'https://drivetothetarget.web.ctfcompetition.com'
TOKEN = 'gAAAAABdDslkg6JZSbI_0VfLkHWd17NX18r4kBZqPSuyc67-PD7Ca6LOfup0WiL8OobEHrXbE1WeYZ4zEx282dpG630uhr9EtL-W7CiK9vQ8VKYsqZVxYCqPnw1QHbs8hWj4hXpvGzUW'

LAT = None
LON = None

#while True:
#    get_coords()
#    move()

#def get_coords()

PARAMS = {'lat': 0.0, 'lon': 0.0, 'token': TOKEN} 
r = requests.get(url=URL, params=PARAMS)

tree = lxml.html.parse(r.text)
root = tree.getroot()
for form in root.xpath('//form[@method="get"]'):
    for field in form.getchildren():
        if 'name' in field.keys():
            print(field.get('name'))

print(r.text)


