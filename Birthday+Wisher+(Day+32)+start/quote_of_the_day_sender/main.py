import smtplib
import random
import datetime as dt

email_id = "kai.shekhar@gmail.com"
my_password = ""

curr_time =dt.datetime.now()
day_of_week = curr_time.weekday()
if day_of_week == 6:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(f"Quote of the day {quote}")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=email_id,password=my_password)
        connection.sendmail(
            from_addr=email_id,
            to_addrs="kai.shekhar@gmail.com",
            msg=quote
        )
    
