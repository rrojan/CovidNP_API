# Generated by Django 3.2.3 on 2021-05-20 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_remove_area_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='area',
            name='category',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Total'), (3, 'By District')], default=3),
        ),
        migrations.AlterField(
            model_name='daily',
            name='category',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Total'), (3, 'By District')], default=1),
        ),
        migrations.AlterField(
            model_name='total',
            name='category',
            field=models.IntegerField(choices=[(1, 'Daily'), (2, 'Total'), (3, 'By District')], default=2),
        ),
    ]
