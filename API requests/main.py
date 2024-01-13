import requests
from datetime import datetime

MY_LAT = 53.381130
MY_LONG = -1.470085

#
# # Get request
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)

# response = requests.get(url="https://api.sunrise-sunset.org/json", params={
#     "lat": 52.520008,
#     "lng": 13.404954,
#     "formatted": 0
# })

response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset)
print(sunrise)

time_now = datetime.now()

print(time_now.hour)
