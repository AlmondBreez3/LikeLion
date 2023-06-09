from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic.list import ListView

from .models import Post #같은 파일내에 있어서 .붙임


def index(request):
    return render(request, 'index.html')

def post_list_view(request):
    return render(request, 'posts/post_list.html')
def post_detail_view(request,id):
    return render(request, 'posts/post_detail.html')
def post_create_view(request):
    return render(request, 'posts/post_form.html')
def post_update_view(request,id):
    return render(request, 'posts/post_form.html')
def post_delete_view(request,id):
    return render(request, 'posts/post_confirm_delete.html')


# Create your views here.
def url_view(request):
    print(url_view)
    data = {'code':'001', 'msg':'ok'}
    return HttpResponse('<h1>url_view</h1>')

def url_parameter_view(request,username):
    print('url_parameter_view()')
    print(f'username:{username}')
    print(f'request.GET: {request.GET}')
    return HttpResponse(username)

def function_view(request):
    print(f'request.method: {request.method}')
    if request.method == "GET":
        print(f'request.GET:{request.GET}')
    else:
        print(f'request.POST: {request.POST}')
    return render(request,'view.html')

class class_view(ListView):
    model =Post
    template_name = 'cbv_view.html'
    
def function_list_view(request):
    object_list =Post.objects.all().order_by('-id')
    return render(request, 'cbv_view.html',{'object_list' : object_list})