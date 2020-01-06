from django.shortcuts import render,get_object_or_404

from .models import  Blog

def blog_view(request):
    blog=Blog.objects.all()
    return render(request,'blog/allblogs.html',{"blog":blog})

def blog_detail(request,blog_id):
    blogdetail=get_object_or_404(Blog,pk=blog_id)
    #blog=Blog.objects.get(pk=blog_id)
    return render(request,'blog/blogdetail.html/',{'blog':blogdetail})
