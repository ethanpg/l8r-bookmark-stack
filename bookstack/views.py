from django.shortcuts import render

from bookmarks.views import show_bookmarks


def index(request):
	if (request.user.is_authenticated()):
		return show_bookmarks(request)
	else:
		return render(request, 'bookstack/index.html')

