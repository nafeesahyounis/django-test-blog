from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home(request):
    """A view to return the home page"""

    posts = Post.objects.all()
    categories = Category.objects.all()

    context = {
        'posts': posts,
        'categories': categories
        }
    return render(request, 'blog/index.html', context)

    