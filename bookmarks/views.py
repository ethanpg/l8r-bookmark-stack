from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.utils.cache import patch_cache_control

from bookmarks.models import Bookmark

def no_store(view):
	def inner(*args, **kwargs):
		response = view(*args, **kwargs)
		patch_cache_control(response, no_store=True)
		return response
	return inner


@login_required
@no_store
def push_bookmark(request, url):
	bookmark = Bookmark(user=request.user, url=url)
	Bookmark.objects.push(bookmark)
	context = {
		'bookmarks': Bookmark.objects.get_stack(request.user),
		'new_bookmark': bookmark.url,
	}
	return render(request, 'bookmarks/list.html', context)

@login_required
@no_store
def pop_bookmark(request):
	bookmark = Bookmark.objects.pop(request.user)
	if (bookmark):
		return redirect(bookmark.url)
	else:
		return render(request, 'bookmarks/list.html', {})

@login_required
@no_store
def show_bookmarks(request):
	context = {
		'bookmarks': Bookmark.objects.get_stack(request.user)
	}
	response = render(request, 'bookmarks/list.html', context)
	return response