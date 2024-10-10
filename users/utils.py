import pyotp
from .task import send_async_email
from django.conf import settings


def generate_otp():
    totp = pyotp.TOTP(pyotp.random_base32(), digits=5, interval=300)
    return totp.now()


def get_otp_body():
    return '''
        <!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Your OTP Code</title>
        <style>
            body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
            }
            .container {
            width: 100%;
            max-width: 600px;
            margin: 0 auto;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            .header {
            text-align: center;
            background-color: #4CAF50;
            padding: 10px 0;
            color: #ffffff;
            border-radius: 10px 10px 0 0;
            }
            .header h1 {
            margin: 0;
            font-size: 24px;
            }
            .content {
            padding: 20px;
            text-align: center;
            }
            .content p {
            font-size: 16px;
            color: #333333;
            }
            .otp-code {
            font-size: 32px;
            font-weight: bold;
            color: #4CAF50;
            margin: 20px 0;
            }
            .footer {
            text-align: center;
            padding: 10px 0;
            font-size: 12px;
            color: #999999;
            }
        </style>
        </head>
        <body>

        <div class="container">
            <div class="header">
            <h1>Your OTP Code</h1>
            </div>

            <div class="content">
            <p>Hello,</p>
            <p>We received a request to access your account. Use the following OTP to complete your registration:</p>

            <div class="otp-code">{{otp}}</div>

            <p>If you did not request this, please ignore this email.</p>
            <p>Thank you for using our service!</p>
            </div>

            <div class="footer">
            <p>&copy; 2024 pickBazar. All rights reserved.</p>
            </div>
        </div>

        </body>
        </html>
    '''


def send_otp_email(user_email, otp_code):
    try:
        subject = "Pickbazar OTP Code for registration"
        body = get_otp_body().replace("{{otp}}", otp_code)
        email_from = settings.EMAIL_HOST_USER
        recipient_list = user_email
        send_async_email.delay(subject, body, email_from, recipient_list)
    except Exception as e:
        print(f'Error sending OTP email: {e}')