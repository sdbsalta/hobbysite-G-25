from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Thread, ThreadCategory
from .forms import CommentForm, ThreadForm

from user_management.models import Profile


class ThreadListView(ListView):
    model = Thread
    template_name = 'forum/thread_list.html'
    context_object_name = 'threads'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thread_category'] = ThreadCategory.objects.all()
        return context


class ThreadDetailView(DetailView):
    model = Thread
    template_name = 'forum/thread_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        thread = self.get_object()
        other_threads = Thread.objects.filter(category=thread.category).exclude(pk=thread.pk)
        context['other_threads'] = other_threads
        return context


class ThreadCreateView(CreateView):
    model = Thread
    form_class = ThreadForm
    template_name = 'forum/thread_create.html'
    success_url = reverse_lazy('forum:thread_list')

    def form_valid(self, form):
        form.instance.author = self.request.user.profile
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = context['form']
        form.fields['author'].initial = Profile.objects.get(user=self.request.user)
        form.fields['author'].disabled = True
        
        context['form'] = form
        return context


class ThreadUpdateView(LoginRequiredMixin, UpdateView):
    model = Thread
    template_name = 'forum/thread_create.html'
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
