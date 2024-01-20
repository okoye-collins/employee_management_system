from django.core.mail import EmailMessage
import os
from decouple import config


class Util:
    @staticmethod
    def send_email(data):

        email = EmailMessage(
            subject=data['email_subject'], from_email=config('EMAIL_HOST_USER'), body=data['email_body'], to=[data['to_email']])
        email.send()