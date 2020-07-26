import requests
import json
import pprint
website_url = "https://www.metaweather.com/"
# city = "Bangalore"
search_api = "api/location/search/?query={}"
city = input("enter the city name: ")
search_api = search_api.format(city)
finalurl = website_url+search_api
website_data = requests.get(finalurl).content
print(website_data)
parsed_data = json.loads(website_data)
print(parsed_data)
woID = int(parsed_data[0]["woeid"])

weatherOnId_url = f"api/location/{woID}"
Wfinallink = website_url+weatherOnId_url
weather_data = requests.get(Wfinallink).content
print(weather_data)
parsed_weather_data = json.loads(weather_data)
pprint.pprint(parsed_weather_data)

# for i in range(0,6):
#     date = parsed_weather_data["consolidated_weather"][i]["created"]
#     max_temp = parsed_weather_data["consolidated_weather"][i]["max_temp"]
#     print(date, max_temp)


min_temp = parsed_weather_data["consolidated_weather"][0]["min_temp"]

if min_temp > 20:
    print("t")