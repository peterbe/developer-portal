# Generated by Django 2.2.1 on 2019-06-25 12:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0009_auto_20190625_1122'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['title']},
        ),
    ]
