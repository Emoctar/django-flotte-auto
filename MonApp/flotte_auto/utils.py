import vonage
from django.conf import settings


def envoyer_sms(numero_destinataire, message):
    client = vonage.Client(key=settings.VONAGE_API_KEY, secret=settings.VONAGE_API_SECRET)
    sms = vonage.Sms(client)

    try:
        response = sms.send_message({
            'from': settings.VONAGE_PHONE_NUMBER,
            'to': [numero_destinataire],
            'text': message,
        })

        return response

    except vonage.exceptions.VonageError as e:
        return str(e)


# utils.py
# from django.core.mail import send_mail

# def envoyer_email_notification(sujet, message, destinataires):
#     send_mail(sujet, message, 'moctardiallo1916@gmail.com', destinataires)


from django.core.mail import send_mail

def envoyer_email_notification(sujet, message, destinataires):
    # Spécifiez le contenu HTML dans le paramètre html_message
    send_mail(
        sujet,
        message,  # Vous pouvez laisser le paramètre message vide
        settings.GES_PARC_EMAIL_HOST_USER,  # Remplacez par votre adresse e-mail expéditrice
        destinataires,
        fail_silently=False,
       
        html_message=message  # Spécifiez le contenu HTML ici
    )
    




