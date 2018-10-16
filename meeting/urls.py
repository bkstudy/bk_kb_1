#code=utf8

from django.conf.urls import patterns,include,url

urlpatterns = patterns(
    'meeting.views',
    (r'^$', 'home'),
    (r'^save$', 'save'),
    (r'^getJson$', 'getJson'),

)
