import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from io import BytesIO

def send_email_with_photo(encoded_photo, file_name, receiver_email):
    smtp_server = 'smtp-mail.outlook.com'
    port = 587

    sender_email = 'steganographyproject@outlook.com'
    sender_password = '123Qaz321!'
    subject = 'Test email'

    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    with BytesIO() as buffer:
        encoded_photo.save(buffer, format='PNG')
        image_data = buffer.getvalue()
    image = MIMEImage(image_data, name=file_name)
    message.attach(image)

    with smtplib.SMTP(smtp_server, port) as smtp:
        smtp.starttls()
        smtp.login(sender_email, sender_password)
        smtp.send_message(message)