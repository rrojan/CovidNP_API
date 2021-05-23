# Generated by Django 3.2.3 on 2021-05-22 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0011_area_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='source',
            field=models.URLField(default='https://covid19.mohp.gov.np/'),
        ),
        migrations.AddField(
            model_name='daily',
            name='source',
            field=models.URLField(default='https://covid19.mohp.gov.np/'),
        ),
        migrations.AddField(
            model_name='total',
            name='source',
            field=models.URLField(default='https://covid19.mohp.gov.np/'),
        ),
    ]