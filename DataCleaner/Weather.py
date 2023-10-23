import sys

sys.path.append("Crawl")
from WeatherCrawling import WeatherCrawler

WeatherCrawler = WeatherCrawler()
WeatherCrawler.current_weather()
