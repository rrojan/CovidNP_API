# Generated by Django 3.2.3 on 2021-05-20 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0010_remove_area_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='area',
            name='date_updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
