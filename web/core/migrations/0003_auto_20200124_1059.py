# Generated by Django 3.0.2 on 2020-01-24 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_userprofileinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileinfo',
            name='pincode',
            field=models.CharField(default='', max_length=10),
        ),
        migrations.AddField(
            model_name='userprofileinfo',
            name='state',
            field=models.CharField(default='', max_length=50),
        ),
    ]
