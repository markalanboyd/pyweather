# pyenv activate pyweather-3.11.2

import pip._vendor.requests as requests


API_KEY = "a8399132b50ffa51edbd9b19e1e3a8fa"

weather_params = {
    "lat": 42.9297,
    "lon": 16.8886,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

forecast_response = requests.get(OWM_Endpoint,
                                 params=weather_params)
forecast_response.raise_for_status()
forecast_json = forecast_response.json()

forecast_next_12 = forecast_json["hourly"][0:12]

def check_for_rain(forecast):
    for hour in range(0,12):
        if forecast_next_12[hour]["weather"][0]["id"] < 700:
            return True

if check_for_rain(forecast_next_12):
    print("Rain's a-comin'.")
else:
    print("Clear skies today.")
