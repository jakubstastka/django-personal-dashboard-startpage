from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        for user in User.objects.all():

            for index, board in enumerate(user.boards.all(), start=1):
                board.position = index
                board.save()

                for gindex, group in enumerate(board.bookmark_groups.all(), start=1):
                    group.position = gindex
                    group.moved = False
                    group.save()

                    for bindex, bookmark in enumerate(group.bookmarks.all(), start=1):
                        bookmark.position = bindex
                        bookmark.save()
