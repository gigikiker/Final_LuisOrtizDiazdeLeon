# Generated by Django 4.1.3 on 2022-11-22 07:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curso',
            old_name='comision',
            new_name='indicador',
        ),
        migrations.AddField(
            model_name='curso',
            name='fecha',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
