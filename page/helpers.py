def enumerate_boards(user):
    for index, board in enumerate(user.boards.all().order_by("position"), start=1):
        board.position = index
        board.save()


def enumerate_groups(board):
    for index, group in enumerate(board.bookmark_groups.all().order_by("position"), start=1):
        group.position = index
        group.moved = False
        group.save()


def enumerate_bookmarks(bookmarkgroup):
    for index, bookmark in enumerate(bookmarkgroup.bookmarks.all().order_by("position"), start=1):
        bookmark.position = index
        bookmark.moved = False
        bookmark.save()
