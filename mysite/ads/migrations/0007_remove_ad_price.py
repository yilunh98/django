# Generated by Django 3.1.5 on 2021-04-10 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0006_auto_20210410_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ad',
            name='price',
        ),
    ]
