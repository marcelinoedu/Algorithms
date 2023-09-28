import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(subject, message, to_email):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    smtp_username = 'carneiroassessoriaoficial@gmail.com'
    smtp_password = 'tzkxmmcxsycnwfut'

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(smtp_username, smtp_password)

    server.sendmail(smtp_username, to_email, msg.as_string())

    server.quit()
