from django.views.generic import ListView, DetailView
from .models import Commission

class CommissionListView(ListView):
    model = Commission
    template_name = 'commission_list.html'

class CommentDetailView(DetailView):
    model = Commission
    template_name = 'comment_detail.html'