# Generated by Django 3.2.4 on 2021-07-17 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0005_auto_20210717_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='horaInicio',
            field=models.CharField(choices=[('7:00', '7:00'), ('7:15', '7:15'), ('7:3', '7:30'), ('7:45', '7:45')], default=7, max_length=5),
        ),
    ]
