from django.contrib import admin
from page.models import Board, BookmarkGroup, Bookmark, AccountSettings

# Register your models here.


@admin.register(AccountSettings)
class AccountSettingsAdmin(admin.ModelAdmin):
    list_display = ["user", "object_count"]


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    list_display = ["name", "bookmark_group_count"]


@admin.register(BookmarkGroup)
class BookmarkGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "bookmark_count"]


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]
