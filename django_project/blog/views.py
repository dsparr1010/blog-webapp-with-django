from django.shortcuts import render
# Create your views here.

# Called dictionaries in python, equivalent to objects in JS
posts = [
    {
        'author': 'Deb Diesel',
        'title': 'Blog post 1',
        'content': 'first post content',
        'date_posted': 'May 27th, 2020'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog post 2',
        'content': 'second post content',
        'date_posted': 'March 27th, 2020'
    },
    {
        'author': 'Rhaegar Targaryen',
        'title': 'Blog post 3',
        'content': 'third post content',
        'date_posted': 'May 2nd, 2020'
    }
]

#function to handle Home route

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})


