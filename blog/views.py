from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Post, Category
from django.core.paginator import Paginator

# Create your views here.


def home(request):
    """A view to return the home page"""

    posts = Post.objects.all()
    categories = None
    # pagination using paginator class, set to three posts per page
    paginator = Paginator(posts, 3)
    page_num = request.GET.get('page')
    page = paginator.get_page(page_num)
    # filter for categories
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
    """ A view to show individual post details using slug """

    posts = Post.objects.get(slug=slug)

    context = {
        'posts': posts,
    }

    return render(request, 'blog/post_detail.html', context)
