from django.shortcuts import render,get_object_or_404
from .models import Blog
# Create your views here.
def myblog(request):
    posts=Blog.objects
    return render(request,'blogs/allblogs.html',{'posts':posts})

def detail(request,post_id):
    detailpost = get_object_or_404(Blog,pk=post_id)
    return render(request,'blogs/detail.html',{'blog':detailpost})
