# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-13 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0016_auto_20160930_0645'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatmenu',
            name='max_levels',
            field=models.PositiveSmallIntegerField(choices=[(1, '1: No sub-navigation (flat)'), (2, '2: Allow 1 level of sub-navigation'), (3, '3: Allow 2 levels of sub-navigation'), (4, '4: Allow 3 levels of sub-navigation')], default=1, help_text='The maximum number of levels to display when rendering this menu. The value can be overidden by supplying a different <code>max_levels</code> value to the <code>{% flat_menu %}</code> tag in your templates.', verbose_name='maximum levels'),
        ),
        migrations.AddField(
            model_name='flatmenu',
            name='use_specific',
            field=models.PositiveSmallIntegerField(choices=[(0, 'OFF (Most efficient)'), (1, 'AUTO'), (2, 'TOP_LEVEL'), (3, 'ALWAYS (Least efficient)')], default=1, help_text="Controls how 'specific' pages objects are fetched and used when rendering this menu. This value can be overidden by supplying a different <code>use_specific</code> value to the <code>{% flat_menu %}</code> tag in your templates.", verbose_name='specific page usage'),
        ),
        migrations.AddField(
            model_name='mainmenu',
            name='max_levels',
            field=models.PositiveSmallIntegerField(choices=[(1, '1: No sub-navigation (flat)'), (2, '2: Allow 1 level of sub-navigation'), (3, '3: Allow 2 levels of sub-navigation'), (4, '4: Allow 3 levels of sub-navigation')], default=2, help_text='The maximum number of levels to display when rendering this menu. The value can be overidden by supplying a different <code>max_levels</code> value to the <code>{% main_menu %}</code> tag in your templates.', verbose_name='maximum levels'),
        ),
        migrations.AddField(
            model_name='mainmenu',
            name='use_specific',
            field=models.PositiveSmallIntegerField(choices=[(0, 'OFF (Most efficient)'), (1, 'AUTO'), (2, 'TOP_LEVEL'), (3, 'ALWAYS (Least efficient)')], default=1, help_text="Controls how 'specific' pages objects are fetched and used when rendering this menu. This value can be overidden by supplying a different <code>use_specific</code> value to the <code>{% main_menu %}</code> tag in your templates.", verbose_name='specific page usage'),
        ),
        migrations.AlterField(
            model_name='mainmenu',
            name='site',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='main_menu', to='wagtailcore.Site'),
        ),
    ]
