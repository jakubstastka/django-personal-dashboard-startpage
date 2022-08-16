from django.urls import path
from .views import BoardList, BoardCreateView, BoardDeleteView, BoardUpdateView

urlpatterns = [
    path('', BoardList.as_view(), name='home'),
    path('board/create', BoardCreateView.as_view(), name='add-board'),
    path('board/<int:pk>/update/', BoardUpdateView.as_view(), name='update-board'),
    path('board/<int:pk>/delete/', BoardDeleteView.as_view(), name='delete-board')
]
