# Generated by Django 2.2.1 on 2019-06-12 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0019_auto_20190611_1453'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-date']},
        ),
    ]
