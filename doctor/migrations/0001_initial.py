# Generated by Django 4.0.2 on 2022-03-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('d_ssn', models.CharField(max_length=50)),
                ('d_password', models.CharField(max_length=50)),
                ('d_fname', models.CharField(max_length=50)),
                ('d_lname', models.CharField(max_length=50)),
                ('d_email', models.EmailField(default='medrecsite@bme.com', max_length=254)),
                ('d_phone', models.CharField(max_length=50)),
                ('d_address', models.CharField(blank=True, max_length=70, null=True)),
                ('d_city', models.CharField(max_length=70)),
                ('d_photo', models.ImageField(default='media/doctor/download.png', upload_to='media/doctor')),
            ],
            options={
                'ordering': ['d_ssn'],
            },
        ),
    ]
