# Generated by Django 4.2.4 on 2023-11-06 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("flotte_auto", "0009_maintenance_en_cours"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="consommationcarburant",
            name="vehicule",
        ),
        migrations.AddField(
            model_name="consommationcarburant",
            name="vehicule",
            field=models.ManyToManyField(to="flotte_auto.vehicule"),
        ),
    ]
