# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0002_auto_20150909_1326'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(null=True, max_length=254)),
            ],
        ),
        migrations.RemoveField(
            model_name='charity',
            name='comments',
        ),
        migrations.AddField(
            model_name='charity',
            name='logo',
            field=models.URLField(default='http://media.makerble.com.s3-eu-west-1.amazonaws.com/production/storage/charities/143/logos/small/SCT_logo.jpeg?1425474633', null=True),
        ),
        migrations.AddField(
            model_name='comments',
            name='charity',
            field=models.ForeignKey(to='charity.Charity'),
        ),
    ]
