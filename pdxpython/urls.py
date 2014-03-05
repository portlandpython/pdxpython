from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pdxpython.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # index page
    url(r'^$', 'apps.home.views.index', name='index'),

    # admin
    url(r'^admin/', include(admin.site.urls)),
)
