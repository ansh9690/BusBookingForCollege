# Generated by Django 3.0.8 on 2020-07-26 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20200726_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookingdetails',
            name='status',
            field=models.CharField(choices=[('B', 'Booked'), ('C', 'Cancelled')], max_length=2),
        ),
    ]
