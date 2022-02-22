# Generated by Django 3.1.3 on 2022-02-22 09:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0012_auto_20211119_1656"),
    ]

    operations = [
        migrations.CreateModel(
            name="Discharge",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateField(auto_now_add=True)),
                ("updated_at", models.DateField(auto_now=True)),
                ("date", models.DateField()),
                ("aware_of_mesh", models.BooleanField()),
                ("infection", models.BooleanField()),
                (
                    "episode",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="discharge",
                        to="registry.episode",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Discharges",
            },
        ),
    ]
