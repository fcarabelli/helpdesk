# Generated by Django 2.2.17 on 2020-12-14 14:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, validators=[django.core.validators.RegexValidator(message='Se permiten entre 9 y 15 números', regex='^\\d{9,15}$')]),
        ),
    ]
