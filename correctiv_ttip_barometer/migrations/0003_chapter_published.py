# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correctiv_ttip_barometer', '0002_chapter_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='published',
            field=models.BooleanField(default=False),
        ),
    ]
