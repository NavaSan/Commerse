# Generated by Django 5.0.7 on 2024-07-23 16:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_remove_listing_category_listing_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='dateCreation',
            field=models.DateTimeField(default=datetime.datetime(2024, 7, 23, 10, 7, 50, 789348)),
        ),
    ]
