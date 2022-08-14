from django.contrib import admin
from page.models import Board, BookmarkGroup, Bookmark

# Register your models here.


class BoardAdmin(admin.ModelAdmin):
    list_display = ["name", "bookmark_group_count"]


class BookmarkGroupAdmin(admin.ModelAdmin):
    list_display = ["name", "bookmark_count"]


class BookmarkAdmin(admin.ModelAdmin):
    list_display = ["name", "url"]


admin.site.register(Board, BoardAdmin)
admin.site.register(BookmarkGroup, BookmarkGroupAdmin)
admin.site.register(Bookmark, BookmarkAdmin)
