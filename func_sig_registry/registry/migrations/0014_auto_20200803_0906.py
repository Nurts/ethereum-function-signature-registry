# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2020-08-03 09:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0013_auto_20160805_0446'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventSignature',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('text_signature', models.TextField(unique=True, validators=[django.core.validators.MinLengthValidator(3)])),
                ('bytes_signature', models.BinaryField(max_length=32, unique=True, validators=[django.core.validators.MinLengthValidator(32)])),
                ('hex_signature', models.CharField(max_length=64, unique=True, validators=[django.core.validators.MinLengthValidator(64)])),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='eventsignature',
            unique_together=set([('text_signature', 'bytes_signature')]),
        ),
    ]