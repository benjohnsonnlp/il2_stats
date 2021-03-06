# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-04 20:08
from __future__ import unicode_literals

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import stats.models


class Migration(migrations.Migration):

    dependencies = [
        ('squads', '0002_auto_20160321_1741'),
        ('stats', '0013_profile_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Squad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(db_index=True, default=0)),
                ('rating', models.IntegerField(db_index=True, default=0)),
                ('sorties_total', models.IntegerField(default=0)),
                ('sorties_coal', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), default=stats.models.default_coal_list, size=None)),
                ('sorties_cls', django.contrib.postgres.fields.jsonb.JSONField(default=stats.models.default_sorties_cls)),
                ('coal_pref', models.IntegerField(choices=[(0, 'neutral'), (1, 'Allies'), (2, 'Axis')], default=0)),
                ('flight_time', models.IntegerField(db_index=True, default=0)),
                ('bailout', models.IntegerField(default=0)),
                ('wounded', models.IntegerField(default=0)),
                ('dead', models.IntegerField(default=0)),
                ('captured', models.IntegerField(default=0)),
                ('relive', models.IntegerField(default=0)),
                ('takeoff', models.IntegerField(default=0)),
                ('landed', models.IntegerField(default=0)),
                ('ditched', models.IntegerField(default=0)),
                ('crashed', models.IntegerField(default=0)),
                ('in_flight', models.IntegerField(default=0)),
                ('shotdown', models.IntegerField(default=0)),
                ('respawn', models.IntegerField(default=0)),
                ('disco', models.IntegerField(default=0)),
                ('ak_total', models.IntegerField(db_index=True, default=0)),
                ('ak_assist', models.IntegerField(default=0)),
                ('gk_total', models.IntegerField(db_index=True, default=0)),
                ('fak_total', models.IntegerField(default=0)),
                ('fgk_total', models.IntegerField(default=0)),
                ('ce', models.FloatField(default=0)),
                ('kd', models.FloatField(db_index=True, default=0)),
                ('kl', models.FloatField(default=0)),
                ('ks', models.FloatField(default=0)),
                ('khr', models.FloatField(db_index=True, default=0)),
                ('gkd', models.FloatField(default=0)),
                ('gkl', models.FloatField(default=0)),
                ('gks', models.FloatField(default=0)),
                ('gkhr', models.FloatField(default=0)),
                ('wl', models.FloatField(default=0)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='stats', to='squads.Squad')),
                ('tour', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='stats.Tour')),
            ],
            options={
                'ordering': ['-id'],
                'db_table': 'squads_stats',
            },
        ),
        migrations.AlterUniqueTogether(
            name='squad',
            unique_together=set([('profile', 'tour')]),
        ),
    ]
