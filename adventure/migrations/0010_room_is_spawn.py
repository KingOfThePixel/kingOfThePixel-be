# Generated by Django 3.0.3 on 2020-03-04 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0009_auto_20200304_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='is_spawn',
            field=models.BooleanField(default=False),
        ),
    ]