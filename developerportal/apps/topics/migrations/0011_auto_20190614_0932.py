# Generated by Django 2.2.1 on 2019-06-14 09:32

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0010_topic_get_started'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='get_started',
            field=wagtail.core.fields.StreamField([('panel', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('description', wagtail.core.blocks.TextBlock()), ('buttonText', wagtail.core.blocks.CharBlock()), ('buttonUrl', wagtail.core.blocks.PageChooserBlock())]))]),
        ),
    ]
