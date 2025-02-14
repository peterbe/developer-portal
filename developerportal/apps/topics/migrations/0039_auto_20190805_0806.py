# Generated by Django 2.2.3 on 2019-08-05 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0038_topic_latest_articles_count'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='latest_articles_count',
            field=models.IntegerField(choices=[(3, '3'), (6, '6'), (9, '9')], default=3, help_text='The number of articles to display for this topic.'),
        ),
    ]
