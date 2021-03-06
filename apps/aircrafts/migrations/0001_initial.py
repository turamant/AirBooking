# Generated by Django 4.0.4 on 2022-04-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Aircraft',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_code', models.CharField(max_length=3, unique=True)),
                ('model', models.JSONField()),
                ('range', models.PositiveIntegerField()),
            ],
        ),
    ]
