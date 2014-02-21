from django.conf.urls import patterns, url

from bookmarks import views

urlpatterns = patterns('',
	url(r'^pop/?$', views.pop_bookmark, name='pop_bookmark'),
	url(r'^(?P<url>.*)$', views.push_bookmark, name="push_bookmark"),
)