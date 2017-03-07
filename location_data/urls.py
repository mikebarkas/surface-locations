from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.StateSelect.as_view(), name='state-select'),
    url(r'^api-json/$', views.api_json, name='api-json'),
    url(r'^city-search/$', views.CitySearch.as_view(), name='city-search'),
    url(r'^(?P<state>[\w]{2})/$', views.city_list, name='city-list'),
    url(r'^(?P<state>[\w]{2})/(?P<city>[\w-]+)/$', views.city_detail, name='city-detail'),
]
