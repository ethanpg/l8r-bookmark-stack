from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.cache import add_never_cache_headers, patch_cache_control

from bookmarks.models import Bookmark

def push_bookmark(request, url):
	bookmark = Bookmark(url=url)
	Bookmark.objects.push(bookmark)
	return HttpResponse("Pushed new bookmark '%s'." % url)


def pop_bookmark(request):
	bookmark = Bookmark.objects.pop()
	if (bookmark):
		response = HttpResponse(
			"<html><script>window.location='%s'</script></html" % bookmark.url)
	else:
		response = HttpResponse("No more bookmarks.")
	patch_cache_control(response, no_store=True)
	return response