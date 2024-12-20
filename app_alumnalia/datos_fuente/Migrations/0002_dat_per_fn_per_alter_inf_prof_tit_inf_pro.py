# Generated by Django 5.1.3 on 2024-12-11 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_alumnalia', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dat_per',
            name='fn_per',
            field=models.CharField(max_length=10, null=True, verbose_name='fecha de nacimiento de la persona'),
        ),
        migrations.AlterField(
            model_name='inf_prof',
            name='tit_inf_pro',
            field=models.IntegerField(choices=[('1', 'Técnico/a'), ('2', 'Grado universitario'), ('3', 'Máster'), ('4', 'Doctorado'), ('5', 'Doctorado'), (6, 'especificar')], default='1', max_length=2, verbose_name='Título académico más alto obtenido'),
        ),
    ]
