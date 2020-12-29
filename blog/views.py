from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home(request):
    """A view to return the home page"""

    posts = Post.objects.all()

    context = {
        'posts': posts,
        }
    return render(request, 'blog/index.html', context)

    