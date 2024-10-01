
import datetime as dt
import random as rnd
import smtplib
import pandas as pd


now = dt.datetime.now()
today_day = now.day
today_month = now.month


birth_data = [
    ["Dawood Rizwan", "dawood.rizwan@outlook.com", 1990, today_month, today_day],
    ["Friend1", "dawood85@hotmail.com", 1985, 12, 15],
    ["Friend2", "friend2@email.com", 1992, 3, 10],
    ["Family1", "family1@email.com", 1980, 8, 29]
]

# with open("birthdays.csv", "a") as data_file:
#     write = csv.writer(data_file)
#     data = [write.writerow(row) for row in birth_data]
#     print(data)




df = pd.read_csv("birthdays.csv")


today_tuple = (today_month, today_day)

birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in df.iterrows()}

if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_location = f"letter_templates/letter_{rnd.randint(1,3)}.txt"
    with open(file_location, "r") as letter_file:
        contents = letter_file.read()
        contents =  contents.replace("[NAME]", birthday_person['name'])



my_email = "senderemailservice23.1@gmail.com"
password = "kqprjgdsjnfzxtsu"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email, to_addrs=birthday_person['email'],
                        msg=f"Subject: Happy Birthday!\n\n {contents}")

