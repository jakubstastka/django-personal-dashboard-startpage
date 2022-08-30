def enumerate_boards(user):
    for index, board in enumerate(user.boards.all().order_by("position"), start=1):
        board.position = index
        board.save()


def enumerate_groups(board):
    for index, group in enumerate(board.boards.all().order_by("position"), start=1):
        group.position = index
        group.save()
