from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from .models import Board

# Create your views here.


class BoardList(LoginRequiredMixin, ListView):
    model = Board

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset
