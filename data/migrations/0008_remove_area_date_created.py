# Generated by Django 3.2.3 on 2021-05-19 12:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_auto_20210519_1831'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='area',
            name='date_created',
        ),
    ]