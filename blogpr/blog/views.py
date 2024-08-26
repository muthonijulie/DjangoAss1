from django.shortcuts import render,get_object_or_404
from .models import Post


# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    return render(request,'blog/list.html',{'posts':posts})

def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/detail.html',{'post':post})

