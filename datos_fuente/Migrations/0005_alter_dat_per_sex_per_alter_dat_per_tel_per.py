# Generated by Django 5.1.3 on 2024-12-11 15:19

import app_alumnalia.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alumnalia', '0004_alter_inf_prof_cert_inf_pro_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dat_per',
            name='sex_per',
            field=models.IntegerField(choices=[('', 'Seleccione una opción'), ('1', 'Mujer'), ('2', 'Hombre'), ('3', 'Prefiero no específicar'), ('4', 'Otro')], default='', verbose_name='Género de la persona'),
        ),
        migrations.AlterField(
            model_name='dat_per',
            name='tel_per',
            field=models.IntegerField(null=True, validators=[app_alumnalia.models.validar_longitud_nueve], verbose_name='Teléfono de la persona'),
        ),
    ]