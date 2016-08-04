# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-08-04 19:24
from __future__ import unicode_literals

from django.db import migrations


def populate_bytes4_signature(apps, schema_editor):
    Signature = apps.get_model('registry', 'Signature')
    BytesSignature = apps.get_model('registry', 'BytesSignature')

    for signature in Signature.objects.all():
        signature.bytes_signature_id = None
        signature.save()

    bytes_signatures_to_remove = BytesSignature.objects.filter(
        signature__isnull=True,
    )
    if bytes_signatures_to_remove.exists():
        print("Removing {0} abandoned bytes signatures".format(
            bytes_signatures_to_remove.count()
        ))
        bytes_signatures_to_remove.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('registry', '0007_auto_20160804_1929'),
    ]

    operations = [
        migrations.RunPython(populate_bytes4_signature),
    ]
