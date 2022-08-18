from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Positioned(models.Model):
    position = models.PositiveSmallIntegerField(default=0)

    class Meta:
        abstract = True
        ordering = ('position',)


class Timestamped(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ("created",)


class Named(models.Model):
    name = models.TextField(default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Board(Positioned, Timestamped, Named):
    description = models.TextField(default="")
    user = models.ForeignKey(User, related_name="boards", on_delete=models.CASCADE)

    @property
    def bookmark_group_count(self):
        return self.bookmark_groups.count()


class BookmarkGroup(Positioned, Timestamped, Named):
    board = models.ForeignKey(Board, related_name="bookmark_groups", on_delete=models.CASCADE)

    @property
    def bookmark_count(self):
        return self.bookmarks.count()


class Bookmark(Positioned, Timestamped, Named):
    url = models.URLField(default="")
    bookmark_group = models.ForeignKey(BookmarkGroup, related_name="bookmarks", on_delete=models.CASCADE)

