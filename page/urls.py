from django.urls import path
from .views import BoardList

urlpatterns = [
    path('', BoardList.as_view(), name='home'),
]
