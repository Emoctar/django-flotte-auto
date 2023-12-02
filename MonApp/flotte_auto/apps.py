from django.apps import AppConfig


class FlotteAutoConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "flotte_auto"

    def ready(self):
        import flotte_auto.signals




# apps.py

