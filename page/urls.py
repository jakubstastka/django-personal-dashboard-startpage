from django.urls import path
from .views import BoardList, BoardCreateView, BoardDeleteView, BoardUpdateView, BookmarkGroupCreateView, \
    BookmarkCreateView, BookmarkGroupDeleteView, BookmarkDeleteView, BookmarkGroupUpdateView, BookmarkUpdateView, \
    hide_board, unhide_board, reorder_items_by_one, BookmarkGroupDetailView

urlpatterns = [
    path('', BoardList.as_view(), name='home'),
    path('board/create', BoardCreateView.as_view(), name='add-board'),
    path('board/<int:pk>/update/', BoardUpdateView.as_view(), name='update-board'),
    path('board/<int:pk>/delete/', BoardDeleteView.as_view(), name='delete-board'),
    path('board/<int:pk>/hide/', hide_board, name='hide-board'),
    path('board/<int:pk>/unhide/', unhide_board, name='unhide-board'),
    path('move/<int:pk>/<str:new_position>/<str:item>', reorder_items_by_one, name='reorder-items-by-one'),
    path('bookmarkgroup/<int:pk>/create/', BookmarkGroupCreateView.as_view(), name='add-bookmark-group'),
    path('bookmarkgroup/<int:pk>/update/', BookmarkGroupUpdateView.as_view(), name='update-bookmark-group'),
    path('bookmarkgroup/<int:pk>/delete/', BookmarkGroupDeleteView.as_view(), name='delete-bookmark-group'),
    path('bookmarkgroup/<int:pk>/edit/', BookmarkGroupDetailView.as_view(), name='edit-bookmark-group'),
    path('bookmark/<int:pk>/create/', BookmarkCreateView.as_view(), name='add-bookmark'),
    path('bookmark/<int:pk>/update/', BookmarkUpdateView.as_view(), name='update-bookmark'),
    path('bookmark/<int:pk>/delete/', BookmarkDeleteView.as_view(), name='delete-bookmark'),
]
