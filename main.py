import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import json

def sender(subject, message, fromEmail, toEmail, login_pwd):

    msg = MIMEMultipart()
    msg['From'] = fromEmail
    msg['To'] = toEmail
    msg['Subject'] = subject

    body = message
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(senderMail, login_pwd)
    text = msg.as_string()
    server.sendmail(fromEmail, toEmail, text)

if __name__ == '__main__':
    file = open("config.json", encoding='utf-8')
    config = json.load(file)

    senderMail = config['senderEmail']
    senderPassword = config['senderPassword']
    toMail = "memirhansumer@gmail.com" # Emaili göndereceğiniz eposta adresini giriniz

    sender("GitHub", "memirhan", senderMail, toMail, senderPassword)
