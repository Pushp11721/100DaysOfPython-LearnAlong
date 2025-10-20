#TODO : send motivational quotes on monday or present day to test
import random
import datetime as dt
import smtplib

my_email = "Sender's mail"
password = "abcd"

#--------------pick random line from txt file----------------#
with open("quotes.txt",mode="r") as file:
    lines = file.readlines()
    random_line = random.choice(lines)

#--------------select monday---------------------------------#
current = dt.datetime.now()
weekday = current.weekday()
print(weekday)
if weekday==6:
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()  # tls - transport layer security
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
                    to_addrs="receiver mail",
                            msg=f"Subject:Quotes\n\n{random_line}"
        )