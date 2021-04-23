import pandas
import random
import datetime
import smtplib

# mail and pwd
MAIL = 'spotifyhakk88@gmail.com'
PWD = '00990988'

# get data from csv and assign to variables
birthday_frame = pandas.read_csv('birthdays.csv')
name = birthday_frame.name.to_string(index=False)
email = birthday_frame.email.to_string(index=False)
year = int(birthday_frame.year.to_string(index=False))
month = int(birthday_frame.month.to_string(index=False))
day = int(birthday_frame.day.to_string(index=False))

# open random letter and replace it with name
letters = [
    "letter_templates/letter_1.txt",
    "letter_templates/letter_2.txt",
    "letter_templates/letter_3.txt"
]
random_letter = random.choice(letters)
with open(random_letter, 'r') as file:
    data = file.read()
    data = data.replace('[NAME]', f'{name}')

# check if the birthday is now
now = datetime.datetime.now()
if month == now.month and day == now.day:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(MAIL, PWD)
        connection.sendmail(
            from_addr=MAIL,
            to_addrs=email,
            msg=f"Subject: Happy Birthday!!\n\n {data}"
        )
