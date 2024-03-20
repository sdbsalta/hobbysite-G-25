from django.views.generic import ListView, DetailView
from .models import Commission, Comment

class CommissionListView(ListView):
    model = Commission
    template_name = 'commissions_list.html'

class CommissionDetailView(DetailView):
    model = Commission
    template_name = 'commissions_detail.html'
