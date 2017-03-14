from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^create', views.start_poll, name='start_poll'),
    url(r'^(?P<poll_id>[0-9]+)/location/(?P<location_id>[0-9]+)/$', views.get_location, name='get_location'),
    url(r'^(?P<poll_id>[0-9]+)/location/(?P<location_id>[0-9]+)/vote/$', views.vote_location, name='vote_location'),
    url(r'^(?P<poll_id>[0-9]+)/result/$', views.get_result, name='get_result')
]
