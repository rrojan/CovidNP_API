# Generated by Django 3.2.3 on 2021-05-19 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DistrictWise',
            new_name='Area',
        ),
        migrations.AlterModelOptions(
            name='daily',
            options={'verbose_name_plural': 'Dailies'},
        ),
    ]