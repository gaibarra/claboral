# Generated by Django 3.0.7 on 2021-04-28 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cto', '0024_auto_20210428_0927'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partes',
            name='estatusParte',
        ),
    ]
