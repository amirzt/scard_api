# Generated by Django 5.0.6 on 2024-05-27 11:14

import users.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='expire_date',
            field=models.DateTimeField(blank=True, default=users.models.get_yesterday_date, null=True),
        ),
    ]
