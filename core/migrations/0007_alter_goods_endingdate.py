# Generated by Django 4.1.3 on 2022-12-05 07:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_history_alter_goods_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='endingdate',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
