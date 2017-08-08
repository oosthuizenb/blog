# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0007_auto_20161016_1055'),
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='PageFieldExtension',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('subtitle', models.CharField(max_length=255, blank=True)),
                ('background_image', filer.fields.image.FilerImageField(blank=True, null=True, to='filer.Image')),
                ('extended_object', models.OneToOneField(editable=False, to='cms.Page')),
                ('public_extension', models.OneToOneField(null=True, editable=False, related_name='draft_extension', to='custom.PageFieldExtension')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
