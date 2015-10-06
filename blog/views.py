from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from blog.models import Post
from taggit.models import Tag


def blog(request):
    posts = Post.objects.all().order_by('-created')
    return paginate_posts(posts, request)


def blog_tag(request, tag):
    posts = Post.objects.filter(tags__slug__in=[tag]).order_by('-created')
    return paginate_posts(posts, request)


def paginate_posts(posts, request):
    paginator = Paginator(posts, 10)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'blog.html', {'posts': posts})


def blog_post(request, slug):
    slug = slug.replace('/','')
    post = Post.objects.get(slug=slug)
    return render(request, 'post.html', {'post': post})
