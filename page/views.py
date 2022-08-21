from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from .models import Board, BookmarkGroup, Bookmark
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.


class BoardList(LoginRequiredMixin, ListView):
    model = Board

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['name']
    success_url = reverse_lazy('home')


class BoardDeleteView(LoginRequiredMixin, DeleteView):
    model = Board
    success_url = reverse_lazy('home')


class BookmarkGroupCreateView(LoginRequiredMixin, CreateView):
    model = BookmarkGroup
    fields = ['name']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.board = Board.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)


class BookmarkGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkGroup
    fields = ['name']
    success_url = reverse_lazy('home')


class BookmarkGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = BookmarkGroup
    success_url = reverse_lazy('home')


class BookmarkCreateView(LoginRequiredMixin, CreateView):
    model = Bookmark
    fields = ['name', 'url']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.bookmark_group = BookmarkGroup.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']
    success_url = reverse_lazy('home')


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('home')
