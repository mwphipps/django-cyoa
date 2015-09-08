# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cyoa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='display_image',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='display_title',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='image',
            field=models.TextField(default=b'No Image', max_length=42),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='story',
            name='story_title',
            field=models.TextField(default=b'Title', max_length=42),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='story',
            name='story_text',
            field=models.TextField(max_length=2000),
            preserve_default=True,
        ),
    ]
