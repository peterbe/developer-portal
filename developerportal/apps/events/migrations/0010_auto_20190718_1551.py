# Generated by Django 2.2.3 on 2019-07-18 15:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20190718_1424'),
    ]

    operations = [
        migrations.RenameField(
            model_name='events',
            old_name='featured_event',
            new_name='featured',
        ),
    ]
