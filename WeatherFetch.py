import requests
from PIL import Image
import json
import os
from dotenv import load_dotenv

load_dotenv("TextClockAlgo\enviroment.env")
#api_key = os.getenv()
api_key = os.environ.get("SECRET_KEY")
city = 'Johannesburg'
url = "http://api.openweathermap.org/data/2.5/weather?q=Johannesburg&appid=%s&units=metric" % (api_key)

response = requests.get(url)
data = json.loads(response.text)
print(data)
current = data['main']['temp']
iconSet = data['weather']

def getWeatherInfo(iconSet,current):
    iconLink = 'http://openweathermap.org/img/wn/' + str(iconSet[0]['icon']) + ".png"
    image = Image.open(requests.get(iconLink, stream = True).raw)
    description = iconSet[0]['description']
    temp = current

    return image,temp,description

#image,temp,description = getWeatherInfo(iconSet,current)
#image.show()
