# Generated by Django 4.2.4 on 2023-12-27 03:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("flotte_auto", "0013_message"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="itineraire",
            name="conducteur",
        ),
        migrations.RemoveField(
            model_name="itineraire",
            name="vehicule",
        ),
        migrations.RemoveField(
            model_name="message",
            name="recipient",
        ),
        migrations.RemoveField(
            model_name="message",
            name="sender",
        ),
        migrations.RemoveField(
            model_name="noteconducteur",
            name="conducteur",
        ),
        migrations.RemoveField(
            model_name="noteconducteur",
            name="utilisateur",
        ),
        migrations.RemoveField(
            model_name="notification",
            name="destinataire",
        ),
        migrations.RemoveField(
            model_name="performanceconduite",
            name="conducteur",
        ),
        migrations.RemoveField(
            model_name="performanceconduite",
            name="utilisateur",
        ),
        migrations.DeleteModel(
            name="Cout",
        ),
        migrations.DeleteModel(
            name="Itineraire",
        ),
        migrations.DeleteModel(
            name="Message",
        ),
        migrations.DeleteModel(
            name="NoteConducteur",
        ),
        migrations.DeleteModel(
            name="Notification",
        ),
        migrations.DeleteModel(
            name="PerformanceConduite",
        ),
    ]
