# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0006_auto_20150909_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]
