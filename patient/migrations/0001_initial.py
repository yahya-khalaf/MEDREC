# Generated by Django 4.0.2 on 2022-03-12 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_ssn', models.CharField(max_length=50)),
                ('p_password', models.CharField(max_length=50)),
                ('p_fname', models.CharField(default='first name', max_length=50)),
                ('p_lname', models.CharField(default='last name', max_length=50)),
                ('p_email', models.EmailField(default='medrecsite@bme.com', max_length=254)),
                ('p_phone', models.CharField(default='9999999999', max_length=50)),
                ('p_city', models.CharField(default='city', max_length=70)),
                ('p_address', models.CharField(default='address', max_length=50)),
                ('p_height', models.IntegerField(default='000')),
                ('p_weight', models.IntegerField(default='000')),
                ('p_age', models.IntegerField(default='00')),
                ('p_diatype', models.CharField(blank=True, choices=[('type1', 'type1'), ('type2', 'type2')], default='type', max_length=20, null=True)),
                ('p_gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='gender', max_length=20)),
            ],
            options={
                'ordering': ['p_ssn'],
            },
        ),
    ]