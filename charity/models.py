from django.db import models
from django.core.urlresolvers import reverse_lazy
# Create your models here.
classifications = [('animals', 'Animals'),
                   ('cancer', 'Cancer'),
                   ('children', 'Children'),
                   ('homelessness', 'Homelessness'),
                   ('international_aid', 'International Aid'),
                   ('mental_health', 'Mental health'),
                   ('unclassified', 'Unclassified'),
                   ('women', 'Women')]


class Charity(models.Model):
    classification = models.CharField(max_length=200, choices=classifications)
    name = models.CharField(max_length=300)
    description = models.TextField()
    number_of_direct_beneficiaries = models.IntegerField(null=True)
    number_of_indirect_beneficiaries = models.IntegerField(null=True)
    annual_cost = models.FloatField(null=True)
    cost_per_direct_beneficiary = models.FloatField(null=True)
    cost_per_indirect_beneficiary = models.FloatField(null=True)
    source = models.TextField()
    logo = models.URLField(null=True, default="http://media.makerble.com.s3-eu-west-1.amazonaws.com/production/storage/charities/143/logos/small/SCT_logo.jpeg?1425474633")

    def get_absolute_url(self):
        return reverse_lazy('charity-detail', kwargs={'pk': self.id})


class Comment(models.Model):
    charity = models.ForeignKey(Charity)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['-date']