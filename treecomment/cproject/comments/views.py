from django.shortcuts import render
from .models import Post


def base_view(request):
    comments = Post.objects.first().comments.all()
    return render(request, 'base.html', {'comments': comments})
