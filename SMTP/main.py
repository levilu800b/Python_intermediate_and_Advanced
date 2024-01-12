# import smtplib
#
# my_email = "test@gmail.com"
# password = "password"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="testdummy@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")
#     connection.close()

import smtplib
import datetime as dt
import random

MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "password"

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="testdummy@gmail.com", msg=f"Subject:Monday Motivation\n\n{quote}")
        connection.close()
