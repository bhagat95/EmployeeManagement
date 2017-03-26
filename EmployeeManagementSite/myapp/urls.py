from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^fetch_users/(?P<company_id>[\w\-]+)/$', views.fetch_users, name='fetch_users'),
    url(r'^add_company/(?P<company_name>[\w\-]+)/$', views.add_company, name='add_company'),
    url(r'^fetch/$', views.fetch, name='fetch'),
]
