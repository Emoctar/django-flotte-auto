# Generated by Django 4.2.4 on 2023-10-08 17:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Conducteur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("prenom", models.CharField(max_length=255)),
                ("nom", models.CharField(max_length=255)),
                (
                    "numero_permis_conduire",
                    models.CharField(max_length=20, unique=True),
                ),
                ("horaires_travail", models.TextField()),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                ("telephone", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="Vehicule",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("marque", models.CharField(max_length=255)),
                ("modele", models.CharField(max_length=255)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                ("annee_fabrication", models.PositiveIntegerField()),
                (
                    "numéro_immatriculation",
                    models.CharField(max_length=20, unique=True),
                ),
                ("kilometrage", models.PositiveIntegerField()),
                (
                    "typeCarburant",
                    models.CharField(
                        choices=[("Gazoil", "gazoil"), ("Essence", "essence")],
                        max_length=20,
                    ),
                ),
                (
                    "statut",
                    models.CharField(
                        choices=[
                            ("Disponible", "Disponible"),
                            ("En Entretien", "En Entretien"),
                            ("Réservé", "Réservé"),
                            ("Indisponible", "Indisponible"),
                        ],
                        default="Disponible",
                        max_length=20,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReservationVoiture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_demande", models.DateTimeField(auto_now_add=True, null=True)),
                ("date_debut", models.DateTimeField()),
                ("date_fin", models.DateTimeField()),
                ("destination", models.CharField(max_length=200)),
                ("motif", models.TextField()),
                ("statut", models.CharField(default="En attente", max_length=20)),
                (
                    "employe",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("vehicules", models.ManyToManyField(to="flotte_auto.vehicule")),
            ],
        ),
        migrations.CreateModel(
            name="PerformanceConduite",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("note", models.IntegerField()),
                ("commentaire", models.TextField()),
                (
                    "conducteur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.conducteur",
                    ),
                ),
                (
                    "utilisateur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Notification",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type_notification", models.CharField(max_length=255)),
                ("message", models.TextField()),
                ("date_envoi", models.DateTimeField()),
                (
                    "destinataire",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NoteConducteur",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("note", models.IntegerField()),
                ("commentaire", models.TextField()),
                (
                    "conducteur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.conducteur",
                    ),
                ),
                (
                    "utilisateur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Maintenance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_maintenance", models.DateTimeField()),
                ("description", models.TextField()),
                ("cout", models.DecimalField(decimal_places=2, max_digits=10)),
                ("prochaine_maintenance", models.DateTimeField()),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.vehicule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Itineraire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_depart", models.DateTimeField()),
                ("date_arrivee", models.DateTimeField()),
                ("lieu_depart", models.CharField(max_length=255)),
                ("lieu_arrivee", models.CharField(max_length=255)),
                (
                    "conducteur",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.conducteur",
                    ),
                ),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.vehicule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GestionnaireParc",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("numéro_bureau", models.CharField(max_length=20)),
                ("date_embauche", models.DateField()),
                ("telephone", models.IntegerField()),
                ("adresse", models.CharField(max_length=120)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                (
                    "utilisateur",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GestionnaireIntervention",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("service", models.CharField(max_length=255)),
                ("date_embauche", models.DateField()),
                ("telephone", models.IntegerField()),
                ("adresse", models.CharField(max_length=120)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                (
                    "utilisateur",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="GestionnaireConsommation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("département", models.CharField(max_length=255)),
                ("date_embauche", models.DateField()),
                ("telephone", models.IntegerField()),
                ("adresse", models.CharField(max_length=120)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                (
                    "utilisateur",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Employé",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("poste", models.CharField(max_length=255)),
                ("departement", models.CharField(max_length=255)),
                ("telephone", models.IntegerField()),
                ("adresse", models.CharField(max_length=120)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="photos/"),
                ),
                (
                    "reservations",
                    models.ManyToManyField(
                        blank=True, to="flotte_auto.reservationvoiture"
                    ),
                ),
                (
                    "utilisateur",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="DonnéesConsommationCarburant",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "quantité_carburant",
                    models.DecimalField(decimal_places=2, max_digits=8),
                ),
                (
                    "gestionnaire_consommation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.gestionnaireconsommation",
                    ),
                ),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.vehicule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Cout",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("type_cout", models.CharField(max_length=255)),
                ("montant", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField()),
                ("description", models.TextField()),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.vehicule",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Assurance",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("compagnie_assurance", models.CharField(max_length=100)),
                ("numero_police", models.CharField(max_length=50)),
                ("date_debut", models.DateField()),
                ("date_fin", models.DateField()),
                (
                    "prime_annuelle",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                (
                    "vehicule",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="flotte_auto.vehicule",
                    ),
                ),
            ],
        ),
    ]