"""charityevaluator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from charity.views import CharityListView, CharityDetailView, CharityUpdateView, CharityCreateView, IndexView

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name="home"),
    url(r'^charities/$', CharityListView.as_view(), name="charity-list"),
    url(r'^charities/create$', CharityCreateView.as_view(), name="charity-create"),
    url(r'^charities/(?P<pk>[0-9]+)/$', CharityDetailView.as_view(), name='charity-detail'),
    url(r'^charities/(?P<pk>[0-9]+)/update$', CharityUpdateView.as_view(), name='charity-detail-update'),
]
