from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    """A view to return the home page"""

    posts = Post.objects.all()
    categories = None
    paginator = Paginator(posts,3)
    page = paginator.get_page(1)

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            posts = posts.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    context = {
        'posts': posts,
        'current_categories': categories,
        'page': page,
        'count': paginator.count
        }
    return render(request, 'blog/index.html', context)


@ login_required
def post_detail(request, slug):
    """ A view to show individual post details """

    posts = Post.objects.get(slug=slug)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/post_detail.html', context)
