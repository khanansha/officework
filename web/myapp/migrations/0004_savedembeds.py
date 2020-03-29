# Generated by Django 3.0.2 on 2020-01-21 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='SavedEmbeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=15)),
                ('provider_url', models.URLField()),
                ('provider_name', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('html', models.TextField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('author_url', models.URLField()),
                ('author_name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
    ]