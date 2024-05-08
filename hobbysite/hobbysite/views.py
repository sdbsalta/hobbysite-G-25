#hobbysite/views.py
from django.shortcuts import render
from django.views import View

def home(request):
    return render(request, 'home.html')

class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')