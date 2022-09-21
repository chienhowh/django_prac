from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
posts = [
    {'author': 'mike', 'title': 'blog post1',
        'content': 'first post content', 'date_posted': '2022/01/01'},
    {'author': 'Step', 'title': 'blog post2',
     'content': 'second post content', 'date_posted': '2022/01/01'}
]


def home(request):
    context = {'posts': Post.objects.all()}
    return render(request, 'blog/home.html', context)


def about(request):

    return render(request, 'blog/about.html', {'title':'About'})
