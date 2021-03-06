# Generated by Django 3.1.12 on 2021-06-28 03:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Workshop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workshop_id', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('latitude', models.DecimalField(decimal_places=11, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=11, max_digits=15)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date')),
                ('latitude', models.DecimalField(decimal_places=11, max_digits=15)),
                ('longitude', models.DecimalField(decimal_places=11, max_digits=15)),
                ('workshop', models.ManyToManyField(to='api.Workshop')),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='name')),
                ('services', models.ManyToManyField(to='api.Service')),
            ],
        ),
    ]
