# Generated by Django 3.1.3 on 2023-04-11 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0030_auto_20230411_0844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discharge',
            name='discharge_duration',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
