# Generated by Django 4.1.3 on 2022-12-08 01:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_alter_goods_price_now'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='price_now',
            field=models.IntegerField(default=models.IntegerField(default='20000000')),
        ),
    ]
