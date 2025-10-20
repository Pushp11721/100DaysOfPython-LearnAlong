import smtplib

my_email = "sender mail"
password = "abcd"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls() # tls - transport layer security
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="receiver mail",
        msg="Subject:Hello\n\nThis is the body of my email"
    )
