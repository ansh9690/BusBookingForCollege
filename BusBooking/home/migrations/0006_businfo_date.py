# Generated by Django 3.0.8 on 2020-07-19 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_remove_businfo_todaydate'),
    ]

    operations = [
        migrations.AddField(
            model_name='businfo',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]