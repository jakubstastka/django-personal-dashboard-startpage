from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Board
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class BoardList(LoginRequiredMixin, ListView):
    model = Board

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BoardCreateView(CreateView):
    model = Board
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        print(self.request.user)
        form.instance.user = self.request.user
        return super().form_valid(form)


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['name']
