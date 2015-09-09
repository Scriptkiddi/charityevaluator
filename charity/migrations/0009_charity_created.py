# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0008_auto_20150909_1552'),
    ]

    operations = [
        migrations.AddField(
            model_name='charity',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 9, 9, 16, 7, 0, 645728, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
