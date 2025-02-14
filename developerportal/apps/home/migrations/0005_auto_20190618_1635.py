# Generated by Django 2.2.1 on 2019-06-18 16:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('home', '0004_homepagefeaturedarticle'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='header_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='intro',
            field=models.TextField(blank=True, default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='homepage',
            name='subtitle',
            field=models.TextField(blank=True, default='', max_length=250),
        ),
    ]
