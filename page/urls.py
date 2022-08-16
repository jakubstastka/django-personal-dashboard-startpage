from django.urls import path
from .views import BoardList, BoardCreateView

urlpatterns = [
    path('', BoardList.as_view(), name='home'),
    path('board/create', BoardCreateView.as_view(), name='add-board')
]
