from WeatherCrawling import WeatherCrawler
from GrabCrawling import GrabCrawler
import datetime as dt
import sys

sys.path.append("SupportMethod")
from Jsonfile import update, create

# create('./Database/MergeDatabase/mergeDatabase.json', 'data')

###################################################
# Define Destination
dest = "TSN_IAP"


###################################################
# Get the data from API Crawler
WeatherCrawler = WeatherCrawler()
GrabCrawler = GrabCrawler()

weather = WeatherCrawler.current_weather()
grab    = GrabCrawler.go_to(dest)


###################################################
for veh in grab["byVehicle"]:
    rowData = {
        "Day": dt.datetime.now().strftime("%A, %d/%m/%Y"),
        "Time": dt.datetime.now().strftime("%X"),
        "Weather": weather["WeatherText"],
        "Metric": weather["Temperature"]["Metric"]["Value"],
        "Imperial": weather["Temperature"]["Imperial"]["Value"],
        "DepartureText": grab["departureText"],
        "DepartureAddress": grab["departureAddress"],
        "DestinationText": grab["destinationText"],
        "DestinationAddress": grab["destinationAddress"],        
        "Type": veh["type"],
        "Price": veh["price"]
    }
    
    path = "./Database/MergeDatabase/mergeDatabase.json"
    update(rowData, "data", path)
 
