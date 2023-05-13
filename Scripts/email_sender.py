import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = 'smtp-mail.outlook.com'
port = 587
username = 'steganographyproject@outlook.com'
receiver_email = 'damian.lesniok@gmail.com'
password = "123Qaz321!"

message = MIMEMultipart()
message['From'] = username
message['To'] = 'recipient_email@example.com'
message['Subject'] = 'Test email'
body = 'This is a test email sent from Python.'
message.attach(MIMEText(body, 'plain'))

with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()
    server.starttls()
    server.login(username, password)
    server.sendmail(username, receiver_email, message.as_string())