from django.shortcuts import render
from django.views import generic
from .models import Post


# def home(request):
#     return render(request, 'index.html')

class home(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
