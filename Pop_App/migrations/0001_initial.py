# Generated by Django 3.1.5 on 2021-08-31 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pop_Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('character', models.CharField(max_length=30)),
                ('series', models.CharField(max_length=50)),
                ('series_number', models.IntegerField()),
                ('special_edition', models.CharField(max_length=30)),
            ],
        ),
    ]
