# celery.py

from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Réglez la variable d'environnement DJANGO_SETTINGS_MODULE sur 'votre_projet.settings'
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MonApp.settings')

app = Celery('MonApp')

# Chargez les configurations de Celery depuis les paramètres de Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# Découvrez et autochargez les tâches de l'application Django
app.autodiscover_tasks()
