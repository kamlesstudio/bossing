# Generated by Django 3.0.8 on 2021-03-22 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bossing_up', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blackbusiness',
            name='rating_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='blackbusiness',
            name='rating_total',
            field=models.FloatField(default=0),
        ),
    ]
