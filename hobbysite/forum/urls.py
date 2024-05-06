from django.urls import path

from .views import ThreadListView, ThreadDetailView, ThreadCreateView, ThreadUpdateView, CommentCreateView

app_name = 'forum'

urlpatterns = [
    path('threads/', ThreadListView.as_view(), name='thread_list'),
    path('thread/<int:pk>/', ThreadDetailView.as_view(), name='thread_detail'),
    path('thread/add', ThreadCreateView.as_view(), name='thread_create'),
    path('thread/<int:pk>/edit/', ThreadUpdateView.as_view(), name='thread_update'),
    path('thread/create/', ThreadCreateView.as_view(), name='thread_create_view'),
    path('comment/create/<int:pk>/', CommentCreateView.as_view(), name='comment_create_view'),
]