from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author': 'rvp',
        'title': 'First Post',
        'content': 'First post content',
        'date_published': 'March, 18',
    },
    {
        'author': 'john doe',
        'title': 'Second Post',
        'content': 'Second post content',
        'date_published': 'March, 28',
    }
]


def home(request):
    context = {'posts': posts, 'title': 'Blog Home page'}
    return render(request, 'blog/home.html',context)


def about(request):
    return render(request, 'blog/about.html')
