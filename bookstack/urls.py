from django.conf.urls import patterns, include, url, handler404

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'favicon.ico', handler404),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include('bookmarks.urls')),
)
