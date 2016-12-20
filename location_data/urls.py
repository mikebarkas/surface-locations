from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.state_select, name='state-select'),
    url(r'^(?P<state>[\w-]+)/$', views.city_list, name='city-list'),
    url(r'^(?P<state>[\w-]+)/(?P<city>[\w-]+)/$', views.city_detail, name='city-detail'),
]
