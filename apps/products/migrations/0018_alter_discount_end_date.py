# Generated by Django 3.2.9 on 2022-02-02 18:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_alter_discount_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 3, 20, 55, 10, 461034), verbose_name='admin__end_date'),
        ),
    ]
