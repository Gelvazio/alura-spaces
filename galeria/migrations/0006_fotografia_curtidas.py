# Generated by Django 4.1.5 on 2023-03-14 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0005_alter_fotografia_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='curtidas',
            field=models.IntegerField(default=0),
        ),
    ]