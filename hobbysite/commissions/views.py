from django.views.generic import ListView, DetailView
from .models import Commission, Comment

class CommissionListView(ListView):
    model = Commission
    template_name = 'commission_list.html'

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'comment_detail.html'