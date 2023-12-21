# signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail, BadHeaderError
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def envoyer_email_utilisateur(sender, instance, created, **kwargs):
    print("Fonction envoyer_email_utilisateur appelée.")
    if created:
        sujet = 'Compte créé avec succès'
        message = 'Votre compte a été créé avec succès.'
        destinataires = [instance.email]

        try:
            # Envoyer l'e-mail à l'utilisateur
            send_mail(
                sujet,
                message,
                'a.myfleet03@gmail.com',  # Remplacez par votre adresse e-mail
                destinataires,
                fail_silently=False
            )
        except BadHeaderError as e:
            print(f"Erreur lors de l'envoi d'e-mail : {e}")
