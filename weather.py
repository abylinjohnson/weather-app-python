import requests
import json
import sys
url = "https://community-open-weather-map.p.rapidapi.com/weather"

querystring = {"q": sys.argv[1], "lat": "0", "lon": "0", "callback": "test",
               "id": "2172797", "lang": "null", "units": "imperial", "mode": "xml"}

headers = {
    'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com",
    'x-rapidapi-key': "ea9af044a4mshfc2a3293ede13f5p182c17jsn9d2337ed2585"
}

response = requests.request("GET", url, headers=headers, params=querystring)


data = json.loads(response.text[5:-1])
print("Temp:", data['main']['temp'], "°F")
print("Humidity:", data['main']['humidity'], "%")
print("Pressure:", data['main']['pressure'], 'mb')
print("Weather:", data["weather"][0]['description'])
