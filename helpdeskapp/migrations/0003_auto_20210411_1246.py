# Generated by Django 2.2.17 on 2021-04-11 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helpdeskapp', '0002_auto_20201214_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
