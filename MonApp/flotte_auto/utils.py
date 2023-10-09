import vonage
from django.conf import settings


def envoyer_sms(numero_destinataire, message):
    client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
    sms = vonage.Sms(client)

    try:
        response = sms.send_message({
            'from': settings.VONAGE_PHONE_NUMBER,
            'to': numero_destinataire,
            'text': message,
        })

        return response

    except vonage.exceptions.VonageError as e:
        return str(e)


# utils.py
from django.core.mail import send_mail

def envoyer_email_notification(sujet, message, destinataires):
    send_mail(sujet, message, 'moctardiallo1916@gmail.com', destinataires)
