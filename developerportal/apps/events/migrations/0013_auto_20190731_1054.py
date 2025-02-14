# Generated by Django 2.2.3 on 2019-07-31 10:54

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0012_auto_20190725_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='speakers',
            field=wagtail.core.fields.StreamField([('speaker', wagtail.core.blocks.PageChooserBlock(page_type=['people.Person'], required=False)), ('external_speaker', wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.CharBlock(label='Name')), ('job_title', wagtail.core.blocks.CharBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('url', wagtail.core.blocks.URLBlock(label='URL', required=False))], required=False))], blank=True, null=True),
        ),
    ]
