# Generated by Django 4.1.5 on 2023-03-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_fotografia_curtidas'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='visitas',
            field=models.IntegerField(default=0),
        ),
    ]