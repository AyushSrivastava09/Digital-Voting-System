# Generated by Django 4.1.2 on 2022-12-15 15:34

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VotingApp', '0003_alter_aadhaardb_age'),
    ]

    operations = [
        migrations.CreateModel(
            name='registeredUsers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aadhaar', models.CharField(max_length=12, validators=[django.core.validators.MinLengthValidator(12)])),
                ('username', models.CharField(max_length=50)),
                ('mobileFromAadhaar', models.BooleanField()),
                ('mobile', models.CharField(max_length=10, validators=[django.core.validators.MinLengthValidator(10)])),
                ('email', models.EmailField(max_length=254)),
                ('pin', models.CharField(max_length=4, validators=[django.core.validators.MinLengthValidator(4)])),
                ('inVotersList', models.BooleanField(default=False)),
            ],
        ),
    ]
