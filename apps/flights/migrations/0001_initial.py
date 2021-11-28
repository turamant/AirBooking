# Generated by Django 3.2.9 on 2021-11-27 20:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('aircrafts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('flight_id', models.UUIDField(default=uuid.uuid4, help_text='Unique ID', primary_key=True, serialize=False)),
                ('flight_number', models.CharField(max_length=100, unique=True, verbose_name='Номер рейса')),
                ('scheduled_departure', models.CharField(max_length=10, verbose_name='Время вылета по расписанию')),
                ('scheduled_arrival', models.CharField(max_length=10, verbose_name='Время прилета по расписанию')),
                ('status', models.CharField(max_length=10, verbose_name='Статус рейса')),
                ('actual_departure', models.CharField(max_length=10, verbose_name='Время вылета актуальное')),
                ('actual_arrival', models.CharField(max_length=10, verbose_name='Время вылета актуальное')),
                ('aircraft_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flights', to='aircrafts.aircraft', verbose_name='код воздушного судна')),
            ],
        ),
    ]