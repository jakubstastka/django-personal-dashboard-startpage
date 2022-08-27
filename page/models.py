from django.db import models
from django.contrib.auth.models import User
from .mixins import Positioned, Timestamped, Named
from .helpers import enumerate_boards


class Board(Positioned, Timestamped, Named):
    description = models.TextField(default="", blank=True)
    user = models.ForeignKey(User, related_name="boards", on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)

    @property
    def bookmark_group_count(self):
        return self.bookmark_groups.count()

    def save(self, *args, **kwargs):
        if not self.pk:
            enumerate_boards(self.user)
        super().save(*args, *kwargs)


class BookmarkGroup(Positioned, Timestamped, Named):
    board = models.ForeignKey(Board, related_name="bookmark_groups", on_delete=models.CASCADE)

    @property
    def bookmark_count(self):
        return self.bookmarks.count()


class Bookmark(Positioned, Timestamped, Named):
    url = models.URLField(default="")
    bookmark_group = models.ForeignKey(BookmarkGroup, related_name="bookmarks", on_delete=models.CASCADE)

