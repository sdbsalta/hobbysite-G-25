# hobbysite/blog/views.py

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import ArticleForm, CommentForm

from user_management.models import Profile

class ArticleListView(ListView):
    model = Article
    template_name = 'blog/article_list.html'
    context_object_name = 'articles'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['article_category'] = ArticleCategory.objects.all()
        return context

class ArticleDetailView(DetailView):
    model = Article
    template_name = 'blog/article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        
        author_articles = Article.objects.filter(author=self.object.author).exclude(pk=self.object.pk)[:2]
        context['author_articles'] = author_articles
        
        return context

class ArticleCreateView(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'blog/article_form.html'
    success_url = reverse_lazy('blog:article_list')

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
    

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'blog/article_form.html'
    fields = ['title', 'category', 'entry', 'header_image']
    def get_success_url(self):
        return reverse_lazy('blog:article_detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class CommentCreateView(LoginRequiredMixin, View):
    def post(self, request, pk):
        article = get_object_or_404(Article, pk=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.author = request.user.profile
            comment.save()
        return redirect('blog:article_detail', pk=pk)

    
