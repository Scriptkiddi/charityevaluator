# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0007_charity_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='classification',
            field=models.CharField(max_length=200, choices=[('animals', 'Animals'), ('cancer', 'Cancer'), ('children', 'Children'), ('homelessness', 'Homelessness'), ('international_aid', 'International Aid'), ('mental_health', 'Mental health'), ('unclassified', 'Unclassified'), ('women', 'Women')], default='unclassified'),
        ),
        migrations.AlterField(
            model_name='charity',
            name='logo',
            field=models.URLField(null=True),
        ),
    ]
