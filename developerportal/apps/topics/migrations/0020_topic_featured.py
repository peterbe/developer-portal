# Generated by Django 2.2.1 on 2019-06-28 14:17

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0019_merge_20190625_1257'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='featured',
            field=wagtail.core.fields.StreamField([('article', wagtail.core.blocks.PageChooserBlock(page_type=['articles.Article'], required=False)), ('external_page', wagtail.core.blocks.StructBlock([('url', wagtail.core.blocks.URLBlock()), ('title', wagtail.core.blocks.CharBlock()), ('intro', wagtail.core.blocks.TextBlock(required=False)), ('header_image', wagtail.images.blocks.ImageChooserBlock(label='Image'))]))], blank=True, null=True),
        ),
    ]
