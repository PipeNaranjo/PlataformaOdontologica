# Generated by Django 3.2.4 on 2021-07-21 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('citas', '0007_alter_evento_horainicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='precio',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
