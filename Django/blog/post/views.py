from django.shortcuts import render,HttpResponse

def post_index(request):
    return HttpResponse('<h>İndex Page</h>')

def post_detail(request):
    return HttpResponse('<h>Detail Page</h>')

def post_create(request):
    return HttpResponse('<h>Create Page</h>')

def post_update(request):
    return HttpResponse('<h>Update Page</h>')

def post_delete(request):
    return HttpResponse('<h>Delete Page</h>')

