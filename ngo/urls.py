from django.conf.urls import patterns, url
from ngo import views

urlpatterns = patterns('',
	url(r'^$', views.ngo, name='ngo'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.category, name='category'),)