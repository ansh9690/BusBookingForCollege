# Generated by Django 3.0.8 on 2020-07-21 07:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_remove_businfo_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='businfo',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]