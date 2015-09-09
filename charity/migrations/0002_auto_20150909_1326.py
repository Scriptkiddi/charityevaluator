# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('charity', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charity',
            name='annual_cost',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='charity',
            name='cost_per_direct_beneficiary',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='charity',
            name='cost_per_indirect_beneficiary',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='charity',
            name='number_of_direct_beneficiaries',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='charity',
            name='number_of_indirect_beneficiaries',
            field=models.IntegerField(null=True),
        ),
    ]
