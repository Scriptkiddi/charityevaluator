# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0004_auto_20150909_1351'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='charity',
            name='classification',
            field=models.CharField(choices=[('Animals', 'Animals')], max_length=200),
        ),
    ]
