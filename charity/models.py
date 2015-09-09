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
    created = models.DateTimeField(auto_now_add=True)
    classification = models.CharField(max_length=200, choices=classifications, default="unclassified")
    name = models.CharField(max_length=300)
    description = models.TextField()
    number_of_direct_beneficiaries = models.IntegerField(null=True, blank=True)
    number_of_indirect_beneficiaries = models.IntegerField(null=True, blank=True)
    annual_cost = models.FloatField(null=True, blank=True)
    cost_per_direct_beneficiary = models.FloatField(null=True, blank=True)
    cost_per_indirect_beneficiary = models.FloatField(null=True, blank=True)
    source = models.TextField()
    logo = models.URLField(null=True, blank=True)

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