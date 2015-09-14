from django.views.generic import ListView, DetailView, TemplateView
from .models import Charity, Comment
from django.views.generic.edit import UpdateView, CreateView
from djqscsv import render_to_csv_response


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
    paginate_by = 10

    def get_queryset(self):
        queryset = Charity.objects.all().\
            exclude(latest_financial_year__cost_per_direct_beneficiary__isnull=True).\
            order_by('-latest_financial_year__cost_per_direct_beneficiary')
        return queryset

    def get_context_data(self, **kwargs):
        context = super(CharityListView, self).get_context_data(**kwargs)
        for charity in context.get('charity_list'):
            charity.last_financialyear = charity.financialyear_set.order_by('-start_date').first()

        return context


class CharityDetailView(DetailView):

    model = Charity

    def get_context_data(self, **kwargs):
        context = super(CharityDetailView, self).get_context_data(**kwargs)
        context['last_financialyear'] = context['object'].financialyear_set.order_by('-start_date').first()
        context['financialyears'] = context['object'].financialyear_set.all()
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

def get_charities_csv(request):
    queryset = Charity.objects.all()
    return render_to_csv_response(queryset)