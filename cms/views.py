from django.shortcuts import render
from cms.models import Page

def home(request):
    return page(request, 'home')


def page(request, slug):
    try:
        page = Page.objects.get(slug=slug)
        return render(request, 'page.html', {'page': page})
    except:
        return not_found(request)


def not_found(request):
    page = Page.objects.get(slug='404')
    return render(request, 'page.html', {'page': page})
