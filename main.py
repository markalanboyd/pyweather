# pyenv activate pyweather-3.11.2

import pip._vendor.requests as requests
import os

API_KEY = os.environ.get("API_KEY")

weather_params = {
    "lat": 42.9297,
    "lon": 16.8886,
    "appid": API_KEY,
    "exclude": "current,minutely,daily,alerts",
}

OWM_Endpoint = "https://api.openweathermap.org/data/2.8/onecall"

def request_forecast() -> list:
    forecast_response = requests.get(OWM_Endpoint,
                                    params=weather_params)
    forecast_response.raise_for_status()
    forecast_json = forecast_response.json()
    return forecast_json["hourly"][:12]

def check_for_rain(forecast) -> bool:
    for hour in forecast:
        condition_code = int(hour["weather"][0]["id"])
        if condition_code < 700:
            return True

def main() -> None:
    forecast_next_12 = request_forecast()
    if check_for_rain(forecast_next_12):
        print("Rain's a-comin'.")
    else:
        print("Clear skies today.")

if __name__ == "__main__":
    main()