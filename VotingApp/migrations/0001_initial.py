# Generated by Django 4.1.2 on 2022-12-10 19:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aadhaarDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('AadhaarNum', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('DOB', models.DateField()),
                ('Age', models.IntegerField()),
                ('Gender', models.CharField(max_length=20)),
                ('State', models.CharField(max_length=50)),
                ('City', models.CharField(max_length=50)),
                ('Pincode', models.CharField(max_length=20)),
                ('Nationality', models.CharField(max_length=50)),
            ],
        ),
    ]
