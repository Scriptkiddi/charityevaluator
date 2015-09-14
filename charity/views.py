from django.views.generic import ListView, DetailView, TemplateView
from .models import Charity, Comment
from django.views.generic.edit import UpdateView, CreateView
# Create your views here.
from django.db.models import Q, Max


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
        queryset = Charity.objects.all()
        for charity in queryset:
            fyear = charity.financialyear_set.order_by('-start_date').first()

            if not fyear:
                queryset = queryset.exclude(id=charity.id)
                continue
            if not fyear.cost_per_direct_beneficiary and not fyear.cost_per_indirect_beneficiary:
                queryset = queryset.exclude(id=charity.id)

        print(queryset)
        queryset = queryset.annotate(Max('financialyear__cost_per_direct_beneficiary')).order_by('-financialyear__cost_per_direct_beneficiary__max')
        print(queryset)

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