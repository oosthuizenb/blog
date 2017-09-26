# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='social_addon_social', parent_link=True, to='cms.CMSPlugin')),
                ('label', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='SocialIcon',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(primary_key=True, serialize=False, auto_created=True, related_name='social_addon_socialicon', parent_link=True, to='cms.CMSPlugin')),
                ('url_link', models.URLField()),
                ('link_title', models.CharField(max_length=200, blank=True)),
                ('extra_classes', models.CharField(max_length=200, blank=True)),
                ('icon', models.ForeignKey(to='social_addon.Icon')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
