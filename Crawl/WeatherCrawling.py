from Crawling import APICrawling
import sys
import json

sys.path.append("SupportMethod")
from Jsonfile import update, create

class WeatherCrawler:
    with open("./assets/API_WEATHER.json", "r") as fread:
        current_weather_params = json.loads(fread.read())["currentWeather"]
    def __init__(self):
        pass
    def current_weather(self):
        def crawlingCall():
            APICrawler = APICrawling(
                API_KEY=WeatherCrawler.current_weather_params["API_KEY"],
                API_URL=WeatherCrawler.current_weather_params["API_REQUEST"],
                params=WeatherCrawler.current_weather_params["PARAMS"],
            )
            return APICrawler()[0]
        path = "./Database/Weather/Weather.json"
        create(path, "weathers")
        update(crawlingCall(), "weathers", path)
