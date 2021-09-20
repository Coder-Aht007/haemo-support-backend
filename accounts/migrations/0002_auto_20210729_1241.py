# Generated by Django 3.2 on 2021-07-29 12:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_user',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'Apositive'), ('A-', 'Anegative'), ('B+', 'Bpositive'), (
                'B-', 'Bnegative'), ('O+', 'Opositive'), ('O-', 'Onegative'), ('AB+', 'Abpositive'), ('AB-', 'Abnegative')], max_length=3),
        ),
        migrations.AlterField(
            model_name='my_user',
            name='phone_number',
            field=models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(
                message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')]),
        ),
    ]
