# Generated by Django 3.1.3 on 2023-02-13 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0020_auto_20221029_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='episode',
            name='complexity',
            field=models.CharField(choices=[('SIMPLE', 'Simple'), ('INCARCERATED', 'Irreducible'), ('OBSTRUCTED', 'With bowel obstruction'), ('STRANGULATED', 'Strangulated')], max_length=16),
        ),
        migrations.AlterField(
            model_name='episode',
            name='mesh_type',
            field=models.CharField(choices=[('TNMHP', 'TNMHP Mesh'), ('KCMC', 'KCMC Generic Mesh'), ('COMMERCIAL', 'Commercial Mesh'), ('INTERNATIONAL', 'Hernia Internation Mesh')], max_length=16),
        ),
    ]
