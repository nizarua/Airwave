# Generated by Django 2.2.6 on 2019-11-18 04:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airwave', '0003_area_customer_isp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airwaveconfig',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(max_length=50)),
                ('key_code', models.CharField(max_length=50)),
                ('key_value', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'AirwaveConfig',
                'managed': False,
            },
        ),
    ]
