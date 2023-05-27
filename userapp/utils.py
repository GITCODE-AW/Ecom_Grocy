from django.conf import settings
from django.core.mail import send_mail

def send_email_token(email, token):
    try:
        subject = f'Verification for Account {email} Grocy'
        message = f'Do not Reply... Security Code : http://127.0.0.1:8000/user/verify/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except:
        return False
    return True

def send_email_token_forgot(email, token):
    try:
        subject = f'Reset Password for Account {email} Grocy'
        message = f'Do not Reply... Security Link Click On : http://127.0.0.1:8000/user/reset/{token}'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
    except:
        return False
    return True
    