from django.db import models
from django.contrib.auth.models import User
from .mixins import Positioned, Timestamped, Named
from .helpers import enumerate_boards


class Board(Positioned, Timestamped, Named):
    SLATE = "slate"
    GRAY = "gray"
    ZINC = "zinc"
    NEUTRAL = "neutral"
    STONE = "stone"
    RED = "red"
    ORANGE = "orange"
    AMBER = "amber"
    YELLOW = "yellow"
    LIME = "lime"
    GREEN = "green"
    EMERALD = "emerald"
    TEAL = "teal"
    CYAN = "cyan"
    SKY = "sky"
    BLUE = "blue"
    INDIGO = "indigo"
    VIOLET = "violet"
    PURPLE = "purple"
    FUCHSIA = "fuchsia"
    PINK = "pink"
    ROSE = "rose"

    COLOR_CHOICES = [
        (SLATE, "Slate"),
        (GRAY, "Gray"),
        (ZINC, "Zinc"),
        (NEUTRAL, "Neutral"),
        (STONE, "Stone"),
        (RED, "Red"),
        (ORANGE, "Orange"),
        (AMBER, "Amber"),
        (YELLOW, "Yellow"),
        (LIME, "Lime"),
        (GREEN, "Green"),
        (EMERALD, "Emerald"),
        (TEAL, "Teal"),
        (CYAN, "Cyan"),
        (SKY, "Sky"),
        (BLUE, "Blue"),
        (INDIGO, "Indigo"),
        (VIOLET, "Violet"),
        (PURPLE, "Purple"),
        (FUCHSIA, "Fuchsia"),
        (PINK, "Pink"),
        (ROSE, "Rose"),
    ]

    description = models.TextField(default="", blank=True)
    user = models.ForeignKey(User, related_name="boards", on_delete=models.CASCADE)
    hidden = models.BooleanField(default=False)
    color = models.TextField(choices=COLOR_CHOICES, default=NEUTRAL)
    bookmarks_color = models.TextField(choices=COLOR_CHOICES, default=NEUTRAL)

    def get_colors(self):
        return sorted(self.COLOR_CHOICES)

    @property
    def get_current_color(self):
        return self.color.capitalize()

    @property
    def get_current_bookmark_color(self):
        return self.bookmarks_color.capitalize()

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

