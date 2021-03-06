# Generated by Django 3.2.9 on 2021-11-30 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, verbose_name='admin__name_currency')),
                ('code', models.CharField(default='', max_length=20, verbose_name='admin__code')),
                ('symbol_left', models.CharField(blank=True, default='', max_length=6, verbose_name='admin__symbol_left')),
                ('symbol_right', models.CharField(blank=True, default='', max_length=6, verbose_name='admin__symbol_right')),
                ('value', models.DecimalField(decimal_places=4, default=0.0, max_digits=10, verbose_name='admin__value')),
                ('status', models.BooleanField(default=True, max_length=20, verbose_name='admin__status')),
                ('is_default', models.BooleanField(blank=True, default=False, verbose_name='admin__is_default')),
            ],
            options={
                'verbose_name': 'admin__currency',
                'verbose_name_plural': 'admin__currencies',
            },
        ),
    ]
