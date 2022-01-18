import datetime as dt
import pandas as pd
import random
import smtplib

# Today's date
today = dt.datetime.today()

# Reads file containing birthday information
df = pd.read_csv("birthdays.csv")

# For every row in the birthdays.csv file, if today's date aligns with the birth day and birth month of the current row, 
# personalize a randomly chosen letter template and send it to their email listed in the birthdays.csv file
for index, row in df.iterrows():
    if row.month == today.month and row.day == today.day:
        random_number = random.randint(1,3)
        sender_name = "" # <-- Enter your name here
        with open(f"./letter_templates/letter_{random_number}.txt", "r") as letter_file:
            letter_data = letter_file.read()
            letter_data = letter_data.replace('[NAME]', str(row.first_name))
            letter_data = letter_data.replace('[SENDER]', sender_name)

        my_email = "" # <-- Enter your gmail address here // Note : You will have to enable "Less secure app access" in your security settings
        password = "" # <-- Enter your gmail password here

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=f"{row.email}", 
                                msg=f"Subject:Happy Birthday\n\n{letter_data}".encode("utf8")
                                )
