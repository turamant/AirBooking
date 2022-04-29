# Generated by Django 4.0.4 on 2022-04-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('airport_code', models.UUIDField(verbose_name='Код аэропорта')),
                ('airport_name', models.CharField(max_length=100, verbose_name='Имя аэропорта')),
                ('city', models.CharField(max_length=100, verbose_name='Город')),
                ('coordinates', models.CharField(max_length=100, verbose_name='Координаты аэропорта')),
                ('timezone', models.CharField(max_length=100, verbose_name='Часовой пояс')),
            ],
        ),
    ]
