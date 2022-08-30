from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():
            for index, board in enumerate(user.boards.all(), start=1):

                for gindex, group in enumerate(board.bookmark_groups.all(), start=1):

                    for bindex, bookmark in enumerate(group.bookmarks.all(), start=1):
                        bookmark.position = bindex
                        bookmark.save()

                    group.position = gindex
                    group.save()

                board.position = index
                board.save()
