from django.shortcuts import render
from django.utils import timezone
from .models import Post

def post_list(request):
	return render(request, 'blog/post_list.html', {})
    

def a(request):
	posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return render(request, 'blog/A.html', {'posts': posts})


def b(request):
	return render(request, 'blog/B.html', {})

def c(request):
	return render(request, 'blog/C.html', {})

	