# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('correctiv_ttip_barometer', '0003_chapter_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='chapter',
            name='long_title',
            field=models.CharField(default=b'', max_length=512, blank=True),
        ),
    ]
