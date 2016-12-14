from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.state, name='state'),
    url(r'^(?P<state>[\w-]+)/$', views.city_list, name='city-list'),
]

