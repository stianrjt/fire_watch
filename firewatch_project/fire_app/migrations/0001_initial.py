# Generated by Django 3.1.3 on 2020-11-03 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FireData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month', models.CharField(max_length=4)),
                ('day', models.CharField(max_length=4)),
                ('temp', models.FloatField()),
                ('relative_humidity', models.FloatField()),
                ('wind', models.FloatField()),
                ('rain', models.FloatField()),
                ('area', models.FloatField()),
            ],
        ),
    ]
