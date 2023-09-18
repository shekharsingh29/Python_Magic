import random
import smtplib
import datetime as dt
import pandas


today = dt.datetime.now()
today_tuple = (today.month, today.day)
birthdays = pandas.read_csv("birthdays.csv")

birth_dic = {(data_record["month"],data_record["day"]):data_record for (index,data_record) in birthdays.iterrows()}

if today_tuple in birth_dic:
    birthday_person = birth_dic[today_tuple]
    file_path = f"letter_templates/{random.randint(1,3)}.txt"
    with open(file_path) as letter:
        content = letter.read()
        content = content.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user="EMAIL_ID",password="**")
        connection.sendmail(
            from_addr="YOUR_EMAIL_ID",
            to_addrs="RECEIVER",
            msg=f"Subject:Happy Birthday\n\n{content}"
        )    



