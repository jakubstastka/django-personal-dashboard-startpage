from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.db.models import Count
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic.list import ListView

from .enums import BoardColor
from .models import Board, BookmarkGroup, Bookmark
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .helpers import enumerate_boards

# Create your views here.


class BoardList(LoginRequiredMixin, ListView):
    model = Board

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(user=self.request.user)
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        user_bookmarks_count = User.objects.filter(username=self.request.user.username).annotate(total=Count('boards__bookmark_groups__bookmarks'))

        context['user_bookmarks_count'] = user_bookmarks_count.first().total

        return context


class BoardCreateView(LoginRequiredMixin, CreateView):
    model = Board
    fields = ['name', 'description', 'color', 'bookmarks_color']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_colors_choices'] = BoardColor.COLOR_CHOICES
        return context


class BoardUpdateView(LoginRequiredMixin, UpdateView):
    model = Board
    fields = ['name', 'description', 'color', 'bookmarks_color']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_colors_choices'] = BoardColor.COLOR_CHOICES
        return context


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_color'] = BookmarkGroup.objects.get(pk=self.kwargs["pk"]).board.color
        return context


class BookmarkGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = BookmarkGroup
    fields = ['name']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['board_color'] = BookmarkGroup.objects.get(pk=self.kwargs["pk"]).board.color
        return context


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

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark_color'] = BookmarkGroup.objects.get(pk=self.kwargs["pk"]).board.bookmarks_color
        return context


class BookmarkUpdateView(LoginRequiredMixin, UpdateView):
    model = Bookmark
    fields = ['name', 'url']
    success_url = reverse_lazy('home')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['bookmark_color'] = BookmarkGroup.objects.get(pk=self.kwargs["pk"]).board.bookmarks_color
        return context


class BookmarkDeleteView(LoginRequiredMixin, DeleteView):
    model = Bookmark
    success_url = reverse_lazy('home')


class BookmarkGroupDetailView(LoginRequiredMixin, DetailView):
    model = BookmarkGroup
    template_name = "page/bookmarkgroup_editing.html"


@login_required
def hide_board(request, pk):
    user_board = Board.objects.filter(user=request.user).get(id=pk)
    if user_board:
        user_board.hidden = True
        user_board.save()

    return redirect('home')


@login_required
def unhide_board(request, pk):
    user_board = Board.objects.filter(user=request.user).get(id=pk)
    if user_board:
        user_board.hidden = False
        user_board.save()

    return redirect('home')


@login_required
def reorder_boards_by_one(request, pk, new_position):

    user_boards = Board.objects.filter(user=request.user)
    board_to_change_order = user_boards.get(pk=pk)
    board_to_change_order_position = board_to_change_order.position

    if new_position == "up":
        board_to_have_order_changed = user_boards.get(position=board_to_change_order_position+1)

        board_to_change_order.position += 1
        board_to_have_order_changed.position -= 1
    else:
        board_to_have_order_changed = user_boards.get(position=board_to_change_order_position-1)

        board_to_change_order.position -= 1
        board_to_have_order_changed.position += 1

    board_to_change_order.save()
    board_to_have_order_changed.save()

    enumerate_boards(request.user)

    return redirect('home')
