# Generated by Django 2.2.1 on 2019-06-26 13:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0008_featuredperson'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='person',
            options={'ordering': ['title']},
        ),
    ]
