from celery import shared_task
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from django.conf import settings


@shared_task
def send_async_email(subject, body, email_from, recipient_email):
    message = MIMEMultipart()
    message["From"] = email_from
    message["To"] = recipient_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "html"))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)
            server.send_message(message)
            print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")
