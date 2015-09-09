from django.views.generic import ListView, DetailView, TemplateView
from .models import Charity, Comment
from django.views.generic.edit import UpdateView, CreateView
# Create your views here.


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
    fields = ['description',
              'number_of_direct_beneficiaries',
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
              'description',
              'number_of_direct_beneficiaries',
              'number_of_indirect_beneficiaries',
              'annual_cost',
              'cost_per_direct_beneficiary',
              'cost_per_indirect_beneficiary',
              'source',
              'logo']