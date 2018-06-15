import smtplib

from settings import smtp_host, smtp_port, smtp_user, smtp_password

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.login(smtp_user, smtp_password)

def send_mail(to, message):
    server.sendmail(smtp_user, to, message)
