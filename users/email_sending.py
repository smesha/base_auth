from django.core.mail import send_mail
from django.conf import settings


def send_mail_for_password_reset(request, recipients: list):
    send_mail(
        subject=settings.TEXT_FOR_SUBJECT_MAIL,
        message=settings.TEXT_FOR_MESSAGE_MAIL,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=recipients,
        fail_silently=False
    )
