from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Thread, ThreadCategory
from .forms import CommentForm

from user_management.models import Profile


class ThreadListView(LoginRequiredMixin, ListView):
    model = Thread
    template_name = 'thread_list.html'
    context_object_name = 'threads'

    def get_queryset(self):
        user_threads = Thread.objects.filter(author=self.request.user)
        other_threads = Thread.objects.exclude(author=self.request.user)
        categories = ThreadCategory.objects.all()

        threads_by_category = {}
        for category in categories:
            threads = other_threads.filter(category=category)
            threads_by_category[category] = threads

        queryset = list(user_threads) + list(other_threads)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_threads = Thread.objects.filter(author=self.request.user)
        other_threads = Thread.objects.exclude(author=self.request.user)
        categories = ThreadCategory.objects.all()

        threads_by_category = {}
        for category in categories:
            threads = other_threads.filter(category=category)
            threads_by_category[category] = threads

        context['user_threads'] = user_threads
        context['threads_by_category'] = threads_by_category
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()

        author_threads = Thread.objects.filter(author=self.object.author).exclude(pk=self.object.pk)[:2]
        context['author_threads'] = author_threads

        return context


class ThreadCreateView(LoginRequiredMixin, CreateView):
    model = Thread
    template_name = 'thread_create.html'
    fields = ['title', 'category', 'entry', 'image']
    success_url = reverse_lazy('forum:thread_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = 'thread_create.html'
    fields = ['title', 'category', 'entry', 'image']

    def get_success_url(self):
        return reverse_lazy('forum:thread_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        thread = get_object_or_404(Thread, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.thread = thread
            comment.author = request.user
            comment.save()
        return redirect('forum:thread_detail', pk=pk)
