import requests
import smtplib
import os

api_key = os.environ.get("WEATHER_API_KEY")

# parameters to enter into API
parameters = {
    "lat" : 41.015137,
    "lon" : 28.979530,
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}

# calling the API
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
print(response.status_code)
response.raise_for_status()

# storing the JSON data into a variable
weather_data = response.json()

# condition flag
need_umbrella = False

# check if the weather will require an umbrella over the next 12 hours
# in the area specified in the parameters
for i in range (0,12):
    if int(weather_data["hourly"][i]["weather"][0]["id"]) < 700:
        need_umbrella = True

# if you need an umbrella, send yourself an email saying such
if need_umbrella:
    my_email = os.environ.get("TESTING_EMAIL")
    password = os.environ.get("TESTING_EMAIL_PW")
    with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=my_email, 
                                msg="Subject:Umbrella Report\n\nBe sure to bring an umbrella today, you might need it. ☂️".encode("utf8")
                                    )
else:
    print("You should be fine without an umbrella today.")
