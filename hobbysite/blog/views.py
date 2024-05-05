# hobbysite/blog/views.py

from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Article, ArticleCategory
from .forms import CommentForm

class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = 'article_list.html'
    context_object_name = 'articles'

    def get_queryset(self):
        user_articles = Article.objects.filter(author=self.request.user)
        other_articles = Article.objects.exclude(author=self.request.user)
        categories = ArticleCategory.objects.all()

        articles_by_category = {}
        for category in categories:
            articles = other_articles.filter(category=category)
            articles_by_category[category] = articles

        queryset = list(user_articles) + list(other_articles)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user_articles = Article.objects.filter(author=self.request.user)
        other_articles = Article.objects.exclude(author=self.request.user)
        categories = ArticleCategory.objects.all()

        articles_by_category = {}
        for category in categories:
            articles = other_articles.filter(category=category)
            articles_by_category[category] = articles

        context['user_articles'] = user_articles
        context['articles_by_category'] = articles_by_category
        return context


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'article_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        context['comments'] = self.object.comment_set.all()
        
        author_articles = Article.objects.filter(author=self.object.author).exclude(pk=self.object.pk)[:2]
        context['author_articles'] = author_articles
        
        return context

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = 'article_form.html'
    fields = ['title', 'category', 'entry', 'header_image']
    success_url = reverse_lazy('blog:article_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    model = Article
    template_name = 'article_form.html'
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
            comment.author = request.user
            comment.save()
        return redirect('blog:article_detail', pk=pk)

    
