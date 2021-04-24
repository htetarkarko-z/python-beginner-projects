import requests
from datetime import datetime
import smtplib

LAT = 16.787515
LNG = 96.152330
MAIL = 'spotifyhakk88@gmail.com'
PWD = '00990988'
# -----------------------------ISS LOCATION---------------------------------- #
def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if LAT - 5 <= iss_latitude <= LNG + 5 and LNG - 5 <= iss_longitude <= LNG + 5:
        return True

# ---------------------------SUN RISE SET API-------------------------------- #
def is_night():
    parameter = {
        'lat': LAT,
        'lng': LNG,
        'formatted': 0,
    }
    sun_api_response = requests.get(
        'https://api.sunrise-sunset.org/json', params=parameter)
    sun_api_response.raise_for_status()
    data = sun_api_response.json()
    sunrise = int(data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset = int(data['results']['sunset'].split('T')[1].split(':')[0])
    hour_now = datetime.now().hour()
    if hour_now >= sunset and hour_now <= sunrise:
        return True

if is_iss_overhead() and is_night():
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MAIL, password=PWD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=MAIL,
            msg="Subject: Look up"
        )
