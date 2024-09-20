from django.shortcuts import render,get_object_or_404,redirect 
from .models import Post
from .forms import PostCreateForm
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required


# Create your views here.
def post_list(request):
    posts=Post.objects.all()
    paginator=Paginator(posts,4,orphans=4,allow_empty_first_page=True)
   
    page=request.GET.get('page')
    try:
        paginated_posts=paginator.page(page)
    except PageNotAnInteger:
        paginated_posts=paginator.page(1)
    except EmptyPage:
        paginated_posts=paginator.page(paginator.num_pages)
    return render(request,'blog/list.html',{'posts':paginated_posts})

def post_detail(request,id):
    post=get_object_or_404(Post,id=id)
    return render(request,'blog/detail.html',{'post':post})
@login_required
def post_create(request):
    if request.method == 'POST':
        form=PostCreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
            form=PostCreateForm()
           
    return render(request,'blog/create.html',{'form':form})
@login_required
def post_update(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='POST':
        form=PostCreateForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            form.save()
            return redirect('list')
    else:
        form=PostCreateForm(instance=post)

    
    return render(request,'blog/update.html',{'form':form,'post':post})
@login_required
def post_delete(request,id):
    post=get_object_or_404(Post,id=id)
    if request.method=='POST':
        post.delete()
        return redirect('list')
    
    return render(request,'blog/delete.html',{'post':post})

def post_about(request):
    return render(request,'blog/about.html')
