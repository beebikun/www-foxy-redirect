from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^$', 'tlvxNMPortal.views.home', name='home'),
    url(r'^(?P<page>[\s\S]+)/$', 'tlvxNMPortal.views.redirect', name='other'),
)
