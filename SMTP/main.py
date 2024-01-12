import smtplib

my_email = "test@gmail.com"
password = "password"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs="testdummy@yahoo.com", msg="Subject:Hello\n\nThis is the body of my email.")
    connection.close()