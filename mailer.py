import smtplib
from email.mime.text import MIMEText
from email.utils import make_msgid, formatdate

from settings import smtp_host, smtp_port, smtp_user, smtp_password

server = smtplib.SMTP(smtp_host, smtp_port)
server.ehlo()
server.starttls()
server.login(smtp_user, smtp_password)

def send_mail(to, subject, message):
    msg = MIMEText(message)
    msg['From'] = smtp_user
    msg['To'] = to
    msg['Subject'] = subject
    msg['Date'] = formatdate(localtime=True)
    msg['Message-ID'] = make_msgid()
    server.sendmail(smtp_user, to, msg.as_string())
