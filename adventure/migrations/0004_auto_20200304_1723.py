# Generated by Django 3.0.3 on 2020-03-04 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adventure', '0003_auto_20200304_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='sprite',
        ),
        migrations.RemoveField(
            model_name='player',
            name='x',
        ),
        migrations.RemoveField(
            model_name='player',
            name='y',
        ),
    ]