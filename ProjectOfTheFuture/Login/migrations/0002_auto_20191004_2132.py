# Generated by Django 2.2.5 on 2019-10-04 16:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='dateReg',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2019, 10, 4, 21, 32, 52, 559350)),
        ),
    ]
