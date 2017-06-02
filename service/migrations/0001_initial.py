# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('unit_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('fields', jsonfield.fields.JSONField(default=dict)),
                ('itemName', models.CharField(max_length=50)),
                ('data', jsonfield.fields.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='SubService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.Service')),
            ],
        ),
        migrations.CreateModel(
            name='SupportedLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('field', jsonfield.fields.JSONField(default=dict)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='checklist',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='service.SubService'),
        ),
    ]
