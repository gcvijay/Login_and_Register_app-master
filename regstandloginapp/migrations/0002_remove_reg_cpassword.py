# Generated by Django 4.2.10 on 2024-02-14 10:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('regstandloginapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reg',
            name='Cpassword',
        ),
    ]
