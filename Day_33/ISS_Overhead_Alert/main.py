import smtplib
import requests
import time
from datetime import datetime

# Latitude and Longitude that I wish to compare to the position of the ISS
MY_LAT = 38.897675
MY_LNG = -77.036530

# Returns true if the ISS is relatively close, info fetched through API
def iss_close():
    iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
    iss_response.raise_for_status()

    iss_data = iss_response.json()
    longitude = float(iss_data["iss_position"]["longitude"])
    latitude = float(iss_data["iss_position"]["latitude"])

    if MY_LAT - 5 <= latitude <= MY_LAT + 5 and MY_LNG - 5 <= longitude <= MY_LNG + 5:
        return True
    else:
        return False

# Returns true if the sun has set
def is_dark():
    parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
    }

    sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    sun_response.raise_for_status()
    data = sun_response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now().hour

    if sunset <= time_now <= sunrise:
        return True

while True:
    time.sleep(60)
    # If the ISS is close and it's dark outside, sends yourself an email from and to the specified email (+password for connection)
    # telling you to look up and catch the ISS overhead. Checks every 60 seconds. 
    if iss_close() and is_dark():
        my_email = "" # <-- Enter your email address here
        password = "" # <-- Enter your password here

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email, 
                                msg="Subject:Look up!\n\nThe ISS is passing over !".encode("utf8")
                                    )
    else:
        print("Conditions not met")
