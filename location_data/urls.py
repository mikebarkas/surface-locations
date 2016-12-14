from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.state, name='state'),
    url(r'^(?P<state>[\w-]+)/$', views.state_list, name='state-list'),
]

