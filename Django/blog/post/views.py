from django.shortcuts import render,HttpResponse, get_object_or_404
from .models import Post

def post_index(request):
    posts = Post.objects.all()
    return render(request, 'post/index.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    context =  {
                'post' : post
               }
    return render(request, 'post/detail.html', context)

def post_create(request):
    return HttpResponse('<h>Create Page</h>')

def post_update(request):
    return HttpResponse('<h>Update Page</h>')

def post_delete(request):
    return HttpResponse('<h>Delete Page</h>')

