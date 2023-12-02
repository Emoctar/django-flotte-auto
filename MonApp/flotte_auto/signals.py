# signals.py

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail

@receiver(post_save, sender=User)
def envoyer_email_admin(sender, instance, created, **kwargs):
    if created:
        sujet = 'Compte créé avec succès'
        message = 'Votre compte a été créé avec succès.'
        destinataires = [instance.email]
        
        # Envoyer l'e-mail
        send_mail(
            sujet,
            message,
            'a.myfleet03@gmail.com',
            destinataires,
            fail_silently=False
        )
