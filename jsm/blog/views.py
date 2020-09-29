from django.shortcuts import render

# Create your views here.
posts = [
    {
        'author': 'Nyx',
        'title': 'Blog post 1',
        'content': 'First post',
        'date': 'Aug 26 2020'
    },
    {
        'author': 'Jane',
        'title': 'Blog post 2',
        'content': 'Second post',
        'date': 'Aug 27 2020'
    },
]


def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
