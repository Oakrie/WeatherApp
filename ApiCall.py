import requests
import json


class weatherApi():

    def __init__(self):
        jsonFile = "/Users/timvela/Documents/codetime/WeatherApp"

        with open(jsonFile) as jsonData:
            apiData = json.load(jsonData)

        self.link = apiData["apiLink"]
        self.key = apiData["apiKey"]

    def get_weather(self, city):
        # return self.link, self.key
        url = "http://{}{}&APPID={}".format(self.link, city, self.key)
        # url = "http://api.openweathermap.org/data/2.5/weather?id=5992996&APPID=12cd76f5d422a145ad2a91cc91989120"
        try:
            response = requests.get(url)
        except Exception as e:
            response = requests.status_codes(url)

        return response.json()

def main():

    weatherApi.__init__()


if __name__ == "__main__":
    main()
