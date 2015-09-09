# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0005_auto_20150909_1522'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='classification',
            field=models.CharField(choices=[('animals', 'Animals'), ('cancer', 'Cancer'), ('children', 'Children'), ('homelessness', 'Homelessness'), ('international_aid', 'International Aid'), ('mental_health', 'Mental health'), ('unclassified', 'Unclassified'), ('women', 'Women')], max_length=200),
        ),
    ]
