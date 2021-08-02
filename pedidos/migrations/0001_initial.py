# Generated by Django 3.2.4 on 2021-08-02 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=50, unique=True)),
                ('descripcion', models.CharField(blank=True, max_length=80, null=True)),
                ('cantidad', models.IntegerField()),
                ('peso', models.IntegerField(blank=True)),
                ('fechaCaducidad', models.DateField()),
                ('fechaRegistro', models.DateField()),
                ('precio', models.IntegerField()),
                ('estado', models.CharField(choices=[('Verde', 'Verde'), ('Amarillo', 'Amarillo'), ('Rojo', 'Rojo')], max_length=10)),
            ],
            options={
                'verbose_name': 'producto',
                'verbose_name_plural': 'productos',
            },
        ),
    ]