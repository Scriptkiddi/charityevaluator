# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Charity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('classification', models.CharField(default='unclassified', max_length=200, choices=[('animals', 'Animals'), ('cancer', 'Cancer'), ('children', 'Children'), ('homelessness', 'Homelessness'), ('international_aid', 'International Aid'), ('mental_health', 'Mental health'), ('unclassified', 'Unclassified'), ('women', 'Women')])),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('logo', models.URLField(blank=True, null=True)),
                ('country', django_countries.fields.CountryField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='CharityTag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='Name')),
                ('slug', models.SlugField(max_length=100, unique=True, verbose_name='Slug')),
                ('is_offical', models.BooleanField()),
            ],
            options={
                'verbose_name_plural': 'Tags',
                'verbose_name': 'Tag',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('username', models.CharField(max_length=256)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('charity', models.ForeignKey(to='charity.Charity')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='FinancialYear',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number_of_direct_beneficiaries', models.IntegerField(blank=True, null=True)),
                ('number_of_indirect_beneficiaries', models.IntegerField(blank=True, null=True)),
                ('annual_cost', models.FloatField(blank=True, null=True)),
                ('cost_per_direct_beneficiary', models.FloatField(blank=True, null=True)),
                ('cost_per_indirect_beneficiary', models.FloatField(blank=True, null=True)),
                ('source', models.TextField()),
                ('start_date', models.DateTimeField(null=True)),
                ('end_date', models.DateTimeField(null=True)),
                ('charity', models.ForeignKey(to='charity.Charity')),
            ],
        ),
        migrations.CreateModel(
            name='TaggedCharity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(db_index=True, verbose_name='Object id')),
                ('content_type', models.ForeignKey(to='contenttypes.ContentType', related_name='charity_taggedcharity_tagged_items', verbose_name='Content type')),
                ('tag', models.ForeignKey(to='charity.CharityTag', related_name='charity_taggedcharity_items')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='charity',
            name='latest_financial_year',
            field=models.ForeignKey(to='charity.FinancialYear', related_name='latest_year', null=True),
        ),
    ]
