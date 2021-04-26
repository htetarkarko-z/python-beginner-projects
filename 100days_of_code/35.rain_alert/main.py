import requests
end_point = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "0b1c6f0a5355af4d4490cd3479039b11"
weather_params = {
    "lat": 16.862240,
    "lon": 96.120979,
    "appid": api_key,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=end_point, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = int(hour_data["weather"][0]["id"])
    if condition_code < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella")
