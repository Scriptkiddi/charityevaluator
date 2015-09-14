from django.db import models
from django.core.urlresolvers import reverse_lazy
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from django.utils.translation import ugettext_lazy as _

# Create your models here.
classifications = [('animals', 'Animals'),
                   ('cancer', 'Cancer'),
                   ('children', 'Children'),
                   ('homelessness', 'Homelessness'),
                   ('international_aid', 'International Aid'),
                   ('mental_health', 'Mental health'),
                   ('unclassified', 'Unclassified'),
                   ('women', 'Women')]

class CharityTag(TagBase):
    # ... fields here
    is_offical = models.BooleanField()

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    # ... methods (if any) here


class Charity(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    classification = models.CharField(max_length=200, choices=classifications, default="unclassified")
    name = models.CharField(max_length=300)
    description = models.TextField()
    logo = models.URLField(null=True, blank=True)
    country = CountryField()
    #tags = TaggableManager(through='TaggedCharity')
    latest_financial_year = models.ForeignKey('FinancialYear', related_name="latest_year", null=True)

    def get_absolute_url(self):
        return reverse_lazy('charity-detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.name


class TaggedCharity(GenericTaggedItemBase):
    tag = models.ForeignKey('CharityTag',
                            related_name="%(app_label)s_%(class)s_items")


class FinancialYear(models.Model):
    number_of_direct_beneficiaries = models.IntegerField(null=True, blank=True)
    number_of_indirect_beneficiaries = models.IntegerField(null=True, blank=True)
    annual_cost = models.FloatField(null=True, blank=True)
    cost_per_direct_beneficiary = models.FloatField(null=True, blank=True)
    cost_per_indirect_beneficiary = models.FloatField(null=True, blank=True)
    source = models.TextField()
    charity = models.ForeignKey(Charity)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)


class Comment(models.Model):
    charity = models.ForeignKey(Charity)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['-date']