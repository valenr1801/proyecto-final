# Generated by Django 4.1.3 on 2022-12-04 20:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ejemplo', '0002_rename_numero_pasaporte_familiar_numero_dni'),
    ]

    operations = [
        migrations.RenameField(
            model_name='familiar',
            old_name='numero_dni',
            new_name='numero_pasaporte',
        ),
    ]
