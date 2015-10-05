from django.views.generic import ListView, DetailView, TemplateView
from .models import Charity, Comment, FinancialYear
from django.views.generic.edit import UpdateView, CreateView
from djqscsv import render_to_csv_response
from django import forms
from django.contrib.gis.geoip import GeoIP
from django.utils import translation
import pycountry
from djmoney_rates.utils import convert_money
from djmoney.models.fields import MoneyField

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['charities'] = Charity.objects.\
            exclude(logo__isnull=True).\
            exclude(description__isnull=True).\
            order_by('-created')[0:4]
        return context


class CharityListView(ListView):

    model = Charity

    def get_queryset(self):
        queryset = Charity.objects.all().\
            exclude(latest_financial_year__cost_per_direct_beneficiary__isnull=True).\
            order_by('latest_financial_year__cost_per_direct_beneficiary')
        return queryset

    def get_context_data(self, **kwargs):
        t = get_client_ip(self.request)
        currency = get_currency_for_ip(t)
        context = super(CharityListView, self).get_context_data(**kwargs)
        for charity in context.get('charity_list'):
            setattr(charity, 'latest_financial_year', convert_money_object(charity.latest_financial_year, currency))
        context['currency'] = currency
        return context


class CharityDetailView(DetailView):

    model = Charity

    def get_context_data(self, **kwargs):
        currency = get_currency_for_ip(get_client_ip(self.request))
        context = super(CharityDetailView, self).get_context_data(**kwargs)
        context['last_financialyear'] = convert_money_object(context['object'].financialyear_set.order_by('-start_date').first(), currency)
        context['financialyears'] = context['object'].financialyear_set.all()
        for financial_year in context.get('financialyears'):
            convert_money_object(financial_year, currency)
        context['comments'] = context['object'].comment_set.all()
        return context


class CharityUpdateView(UpdateView):
    model = Charity
    fields = ['description',
              'country',
              'logo']
    template_name_suffix = "_update_form"


class CharityCreateView(CreateView):
    model = Charity
    fields = ['classification',
              'name',
              'description',
              'number_of_direct_beneficiaries',
              'number_of_indirect_beneficiaries',
              'annual_cost',
              'cost_per_direct_beneficiary',
              'cost_per_indirect_beneficiary',
              'source',
              'logo']


class FinancialYearUpdateView(UpdateView):
    model = FinancialYear
    fields = ['number_of_direct_beneficiaries',
              'number_of_indirect_beneficiaries',
              'annual_cost',
              'cost_per_direct_beneficiary',
              'cost_per_indirect_beneficiary',
              'source',
              'start_date',
              'end_date']
    template_name_suffix = "_update_form"

    def get_form(self, form_class):
        form = super(FinancialYearUpdateView, self).get_form(form_class)
        form.fields['start_date'].widget.attrs.update({'class': 'datepicker'})
        form.fields['end_date'].widget.attrs.update({'class': 'datepicker'})
        return form


def get_charities_csv(request):
    queryset = Charity.objects.all()
    return render_to_csv_response(queryset)


def get_currency_for_ip(ip):
        g = GeoIP()
        country_lookup = g.country(ip)
        if not country_lookup.get('country_name'):
            country_name = 'United States'
        else:
            country_name = country_lookup.get('country_name')
        country = pycountry.countries.get(name=country_name)
        currency_number = country.numeric
        if country.numeric == 276:
            currency_number = 978
        currency = pycountry.currencies.get(numeric=currency_number)
        return currency.letter


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def convert_money_object(obj, currency):
    for field in obj._meta.get_fields():
        if isinstance(field, MoneyField):
            field_instance = getattr(obj, field.name)
            if field_instance:
                setattr(obj, field.name, convert_money(field_instance.amount,
                                                       field_instance.currency,
                                                       currency))
    return obj
