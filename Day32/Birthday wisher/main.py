#TODO : Birthday wisher
import datetime as dt
import pandas
from random import randint
import smtplib

#Get current date
current = dt.datetime.now()
month = current.month
day = current.day

#Set mail
my_email = "Your e-mail/Sender's e-mail"
password = "abcd"


data = pandas.read_csv("birthdays.csv")
birthday_today = data[(data["month"]==month) & (data["day"]==day)] #Check for birthday on current date

if not birthday_today.empty:
    for _,row in birthday_today.iterrows():
        b_day = row["day"] #Get day of person's birthday
        b_month = row["month"] #Get month for same
        b_name = row["name"] #Get name
        b_mail = row["email"] #Get email of the person

        random_letter_path = f"letter_templates/letter_{randint(1,3)}.txt" #Get path for randomly chosen letter

        with open(random_letter_path,mode="r") as file:
            letter = file.read() #Get that letter using the path

        customized_letter = letter.replace("[NAME]",b_name) # change [NAME] section

        with smtplib.SMTP("smtp.gmail.com", port=587) as connection: #send email using smtp package
            connection.starttls()
            connection.login(user=my_email,password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=b_mail,
                msg=f"Subject:Happy Birthday!!\n\n{customized_letter}"
            )