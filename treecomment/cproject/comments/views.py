from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import CommentForm
from .utils import create_comments_tree

def base_view(request):
    comments = Post.objects.first().comments.all()
    result = create_comments_tree(comments)
    comment_form = CommentForm(request.POST or None)
    return render(request, 'base.html', {'comments': result})


def create_comment(request):
    comment_form = CommentForm(request.POST or None)
    if comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.user = request.user
        new_comment.text = comment_form.cleaned_data['text']
        new_comment.content_type = ContentType.objects.get(model='post')
        new_comment.object_id = 1
        new_comment.parent = None
        new_comment.is_child = False
        new_comment.save()
    return HttpResponseRedirect('/post-comment')

