# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-12 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170312_1438'),
    ]

    operations = [
        migrations.CreateModel(
            name='SelectedLocations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num', models.SmallIntegerField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Location')),
                ('poll', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.Poll')),
            ],
        ),
        migrations.RemoveField(
            model_name='choice',
            name='poll',
        ),
        migrations.AlterField(
            model_name='choice',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polls.SelectedLocations'),
        ),
    ]
