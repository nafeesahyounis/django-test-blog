from django.shortcuts import render
from .models import Post, Category

# Create your views here.

def home(request):
    """A view to return the home page"""

    posts = Post.objects.all()
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = posts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'posts': posts,
        'current_categories': categories
        }
    return render(request, 'blog/index.html', context)

    