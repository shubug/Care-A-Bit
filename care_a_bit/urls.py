from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from care_a_bit import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'care_a_bit.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^donor/', include('donor.urls')),
    url(r'^ngo/', include('ngo.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
