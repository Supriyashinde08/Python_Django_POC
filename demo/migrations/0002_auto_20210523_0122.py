# Generated by Django 3.2.2 on 2021-05-22 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productdetails',
            name='date_added',
        ),
        migrations.RemoveField(
            model_name='productdetails',
            name='gender',
        ),
    ]