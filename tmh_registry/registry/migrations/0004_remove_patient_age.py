# Generated by Django 3.1.3 on 2021-06-07 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("registry", "0003_auto_20210607_1617"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="patient",
            name="age",
        ),
    ]
