# Generated by Django 3.0.8 on 2020-07-21 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20200721_1203'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='businfo',
            name='date',
        ),
    ]
