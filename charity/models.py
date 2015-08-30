from django.db import models

# Create your models here.


class Charity(models.Model):
    classification = models.CharField(max_length=200)7
    name = models.CharField(max_length=300)
    number_of_direct_beneficiaries = models.IntegerField()
    number_of_indirect_beneficiaries = models.IntergerField()
    annual_cost = models.FloatField()
    cost_per_direct_beneficiary = models.FloatField()
    cost_per_indirect_beneficiary = models.FloatField()
    comments = models.TextField()
    source = models.TextField()