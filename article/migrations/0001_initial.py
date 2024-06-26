# Generated by Django 5.0.6 on 2024-05-27 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('content', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='article/')),
                ('read_time', models.IntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_special', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
