# pyenv activate pyweather-3.11.2

import pip._vendor.requests as requests

API_URL = "https://api.openweathermap.org/data/2.8/onecall?lat=42.9297&lon=16.8886&appid=a8399132b50ffa51edbd9b19e1e3a8fa"

forecast_response = requests.get(API_URL)
forecast_response_code = forecast_response.status_code
forecast_json = forecast_response.json()

forecast_next_24 = forecast_json["hourly"][0:25]

for hour in range(0,25):
    if forecast_next_24[hour]["weather"][0]["main"] == "Rain":
        print("Rain's a-comin'")
        break
    else:
        print("Clear skies")
