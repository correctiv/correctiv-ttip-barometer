# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import filer.fields.image
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('status', models.PositiveSmallIntegerField(default=15, choices=[(0, 'Just started.'), (15, 'No agreement in sight.'), (30, "It's complicated."), (60, "There's a first contract draft."), (75, 'Almost there.'), (100, 'The contract is concluded.')])),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated', models.DateTimeField(default=django.utils.timezone.now)),
                ('teaser', models.TextField(blank=True)),
                ('order', models.PositiveIntegerField(default=0)),
                ('body', models.TextField(blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.SET_NULL, default=None, blank=True, to='filer.Image', null=True, verbose_name='image')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]
