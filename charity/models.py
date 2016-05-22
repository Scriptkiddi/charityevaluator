from django.db import models
from django.core.urlresolvers import reverse_lazy
from django_countries.fields import CountryField
from taggit.managers import TaggableManager
from taggit.models import TagBase, GenericTaggedItemBase
from django.utils.translation import ugettext_lazy as _
from moneyed import USD
from djmoney.models.fields import MoneyField
from djmoney_rates.utils import convert_money

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
<<<<<<< HEAD
    classification = models.CharField(max_length=200)
    name = models.CharField(max_length=300)
    number_of_direct_beneficiaries = models.IntegerField()
    number_of_indirect_beneficiaries = models.IntergerField()
    annual_cost = models.FloatField()
    cost_per_direct_beneficiary = models.FloatField()
    cost_per_indirect_beneficiary = models.FloatField()
    comments = models.TextField()
    source = models.TextField()
=======
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
    annual_cost = MoneyField(max_digits=15, decimal_places=2, default_currency='USD', null=True)
    cost_per_direct_beneficiary = MoneyField(max_digits=15, decimal_places=2, default_currency='USD', null=True)
    cost_per_indirect_beneficiary = MoneyField(max_digits=15, decimal_places=2, default_currency='USD', null=True)
    source = models.TextField()
    charity = models.ForeignKey(Charity)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):

        for field in self._meta.fields:
            if isinstance(field, MoneyField):
                field_instance = getattr(self, field.name)
                if not field_instance:
                    continue
                if field_instance.currency != 'USD':
                    setattr(self, field.name, convert_money(field_instance.amount, field_instance.currency, 'USD'))
        super(FinancialYear, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse_lazy('charity-detail', kwargs={'pk': self.charity.id})




class Comment(models.Model):
    charity = models.ForeignKey(Charity)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    username = models.CharField(max_length=256)
    email = models.EmailField(null=True)

    class Meta:
        ordering = ['-date']
>>>>>>> 9a42c3a32ced5e23f968a9ea7ce9a3d8e875e03b
