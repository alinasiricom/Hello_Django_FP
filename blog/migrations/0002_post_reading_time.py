# Generated by Django 4.2.15 on 2024-08-24 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='reading_time',
            field=models.IntegerField(default=3),
        ),
    ]
