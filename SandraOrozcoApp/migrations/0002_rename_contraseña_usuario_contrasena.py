# Generated by Django 3.2.4 on 2021-07-06 21:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SandraOrozcoApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='contraseña',
            new_name='contrasena',
        ),
    ]
