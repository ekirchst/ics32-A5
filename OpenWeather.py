# Evan
# ekirchst@uci.edu
# 59946460
from urllib import request
import json as js
from datetime import datetime
from WebAPI import WebAPI


class OpenWeather(WebAPI):
    '''
    Weather API Class Created to Interact with OpenWeather api
    '''
    def __init__(self, zipcode="92697", ccode="US"):
        '''
        Initializes OpenWeather Object
        Takes in zipcode and ccode
        '''
        self.zip_code = zipcode
        self.country_code = ccode
        self.url = 'https://api.openweathermap.org/data/2.5'

    def load_data(self) -> None:
        '''
        Function to Retrieve Certain Data from the Open Weather API
        '''
        try:
            temp1 = f"{self.url}/weather?zip={self.zip_code},"
            temp2 = f"{self.country_code}&appid={self.apikey}"
            temp = f"{temp1}{temp2}"
            response = request.urlopen(temp)
            re = js.loads(response.read())
            if response.getcode() != 404 or 503:
                self.temperature = re['main']['temp']
                self.high_temperature = re['main']['temp_max']
                self.low_temperature = re['main']['temp_min']
                self.longitude = re['coord']['lon']
                self.latitude = re['coord']['lat']
                self.description = re['weather'][0]['description']
                self.humidity = re['main']['humidity']
                self.sunset = datetime.utcfromtimestamp(
                    re['sys']['sunset']
                    ).strftime('%Y-%m-%d %H:%M:%S')
                self.city = re['name']
            elif response.getcode() == 404:
                print("404 ERROR, API UNAVAILABLE")
            elif response.getcode() == 503:
                print("503 ERROR")
        except request.URLError as e:
            print(f"ERROR {e}")
        except js.JSONDecodeError as e:
            print(f"ERROR {e}")

    def transclude(self, message: str) -> str:
        '''
        Function to Replace Keyword "@weather" with Data from Open Weather API
        '''
        temp = message.lower()
        if "@weather" in temp:
            new = temp.replace("@weather", self.description)
            return new
