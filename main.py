# Project: Desktop Notification App
# Name: Carter E Gamary

# Import statements
import datetime
import time
import requests
from plyer import notification

weatherData = None
try:
    weatherData = requests.get("http://api.weatherapi.com/v1/current.json?key=f0ec325c617c4dacb8c42202220505 &q=68123&aqi=no")
except:
    print("Check internet connection")

if (weatherData != None):
    data = weatherData.json()
    location = data['location']
    current = data['current']
    condition = current['condition']

    # Repeat the loop until program is cancelled
    while(True):
        notification.notify(
            # Title of Notification
            title="Weather on {}".format(datetime.date.today()),
            # Body of Notification
            message="Weather in {city}, {state}\nTemperature (F): {tf}\nCondition: {cond}\nWind: "
                    "{ws}mph in the {wd} direction\n".format(
                city=location['name'],
                state=location['region'],
                tf=current['temp_f'],
                cond=condition['text'],
                ws=current['wind_mph'],
                wd=current['wind_dir']
            ),
            # Weather Notification Icon
            app_icon= "kweather.ico",
            # notification stays for 1 min
            timeout=60
        )

        # Sleeps for 1 day
        # Notification will repeat in 1 day
        time.sleep(60*60*24)

