# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-14 11:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170312_1805'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='selectedlocations',
            unique_together=set([('poll', 'num')]),
        ),
    ]
