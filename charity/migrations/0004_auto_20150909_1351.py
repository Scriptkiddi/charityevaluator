# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0003_auto_20150909_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('charity', models.ForeignKey(to='charity.Charity')),
            ],
        ),
        migrations.RemoveField(
            model_name='comments',
            name='charity',
        ),
        migrations.DeleteModel(
            name='Comments',
        ),
    ]
