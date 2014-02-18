from urllib.parse import urlparse

from django.db import models


class BookmarkManager(models.Manager):
	def top(self):
		top = (Bookmark.objects
			.filter(stack_position__isnull=False)
			.order_by('-stack_position')[:1])
		if (top):
			return top[0]
		else:
			return None

	def push(self, bookmark):
		top = Bookmark.objects.top()
		if (top):
			bookmark.stack_position = top.stack_position + 1
		else:
			bookmark.stack_position = 0
		bookmark.save()

	def pop(self):
		top = Bookmark.objects.top()
		if (top):
			top.stack_position = None
			top.save()
		return top


class Bookmark(models.Model):
	url = models.URLField(primary_key=True, max_length=4096)
	stack_position = models.IntegerField(null=True)

	objects = BookmarkManager()

	def save(self):
		parsed = urlparse(self.url)
		if (not parsed.scheme):
			self.url = 'http://' + self.url
		super().save()

	def __str__(self):
		return "%s [%s]" % (self.url, self.stack_position)

