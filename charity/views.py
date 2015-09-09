from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Charity
from django.views.generic.edit import UpdateView, CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.


class CharityListView(ListView):

    model = Charity

    def get_context_data(self, **kwargs):
        context = super(CharityListView, self).get_context_data(**kwargs)
        return context


class CharityDetailView(DetailView):

    model = Charity

    def get_context_data(self, **kwargs):
        context = super(CharityDetailView, self).get_context_data(**kwargs)
        context['comments'] = context['object'].comment_set.all()
        return context


class CharityUpdateView(UpdateView):
    model = Charity
    fields = ['number_of_direct_beneficiaries',
              'number_of_indirect_beneficiaries',
              'annual_cost',
              'cost_per_direct_beneficiary',
              'cost_per_indirect_beneficiary',
              'source',
              'logo']
    template_name_suffix = "_update_form"


class CharityCreateView(CreateView):
    model = Charity
    fields = ['classification',
              'name',
              'number_of_direct_beneficiaries',
              'number_of_indirect_beneficiaries',
              'annual_cost',
              'cost_per_direct_beneficiary',
              'cost_per_indirect_beneficiary',
              'source',
              'logo']