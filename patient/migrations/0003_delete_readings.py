# Generated by Django 4.0.2 on 2022-02-27 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0002_readings'),
    ]

    operations = [
        migrations.DeleteModel(
            name='readings',
        ),
    ]