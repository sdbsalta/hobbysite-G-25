from django.urls import path
from django.views.generic.base import RedirectView
from .views import ArticleListView, ArticleDetailView

app_name = 'blog'

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('', RedirectView.as_view(url='/blog/articles/')),
]
