# Generated by Django 3.2 on 2021-08-23 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0002_donationrequest_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='donationrequest',
            name='is_complete',
            field=models.BooleanField(default=False),
        ),
    ]
