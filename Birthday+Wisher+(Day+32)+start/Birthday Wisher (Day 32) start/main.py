import smtplib
import datetime as dt
import random

# email_id = "shekharsingh9429@gmail.com"
# my_password = ""

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=email_id,password=my_password)
#     connection.sendmail(
#         from_addr=email_id,
#         to_addrs="kai.shekhar@gmail.com",
#         msg="Hello"
#     )

current_day = dt.datetime.now()


quotes_file = open("quotes.txt")
