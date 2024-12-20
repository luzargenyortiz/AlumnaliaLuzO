# Generated by Django 4.1 on 2024-12-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_alumnalia", "0005_alter_dat_per_sex_per_alter_dat_per_tel_per"),
    ]

    operations = [
        migrations.AddField(
            model_name="inf_prof",
            name="for_imp_esp_inf_pro",
            field=models.CharField(
                default=1,
                max_length=255,
                verbose_name="Especifique que for_imp_inf_pro ha impartido",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="inf_prof",
            name="tit_esp_inf_pro",
            field=models.CharField(
                max_length=30, verbose_name="Especifique tit_inf_pro"
            ),
        ),
    ]
