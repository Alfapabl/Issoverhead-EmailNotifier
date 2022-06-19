import requests
from datetime import datetime
import smtplib
import time
starttime = time.time()


MY_LAT = 9.998910 # Your latitude
MY_LONG = -84.116478 # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.
def iss_position():
    if MY_LAT-5 <= iss_latitude >= MY_LAT-5 and MY_LONG-5 <= iss_latitude >= MY_LONG-5:
        return True
    else:
        return False



parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
hour = time_now.hour

my_email = "test"
my_password = "test"

def email_sender():
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=my_email, password=my_password)
    connection.sendmail(from_addr=my_email, to_addrs="pablo-mendez09@hotmail.com", msg="Look UP ISS on the sky")

def iss_notifier():
    if iss_position() == True and hour in range(sunset, sunrise):
        email_sender()

while True:
    iss_notifier()
    print(iss_position())
    time.sleep(60.0 - ((time.time() - starttime) % 60.0))




