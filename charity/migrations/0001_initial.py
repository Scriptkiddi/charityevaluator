# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('classification', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=300)),
                ('number_of_direct_beneficiaries', models.IntegerField()),
                ('number_of_indirect_beneficiaries', models.IntegerField()),
                ('annual_cost', models.FloatField()),
                ('cost_per_direct_beneficiary', models.FloatField()),
                ('cost_per_indirect_beneficiary', models.FloatField()),
                ('comments', models.TextField()),
                ('source', models.TextField()),
            ],
        ),
    ]
