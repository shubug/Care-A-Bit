from django.conf.urls import patterns, url
from donor import views

urlpatterns = patterns('',
	url(r'^$', views.donor, name='donor'),
    url(r'^signup/$', views.signup, name='signup'), 
)
