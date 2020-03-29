# Generated by Django 3.0.2 on 2020-01-23 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registrationform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('mobile_no', models.CharField(max_length=10)),
                ('password', models.CharField(max_length=30)),
                ('con_password', models.CharField(default='', max_length=30)),
            ],
        ),
    ]
