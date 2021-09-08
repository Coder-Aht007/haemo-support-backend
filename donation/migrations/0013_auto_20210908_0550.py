# Generated by Django 3.2 on 2021-09-08 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donation', '0012_donationrequest_donated_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='donationrequest',
            old_name='donated_by',
            new_name='donor',
        ),
        migrations.RemoveField(
            model_name='donationrequest',
            name='in_progress',
        ),
        migrations.RemoveField(
            model_name='donationrequest',
            name='is_approved',
        ),
        migrations.RemoveField(
            model_name='donationrequest',
            name='is_complete',
        ),
        migrations.RemoveField(
            model_name='donationrequest',
            name='is_rejected',
        ),
        migrations.AddField(
            model_name='donationrequest',
            name='status',
            field=models.IntegerField(choices=[(0, 'Rejected'), (1, 'Pending'), (2, 'Approved'), (3, 'In Progress'), (4, 'Completed')], default=1),
        ),
    ]
