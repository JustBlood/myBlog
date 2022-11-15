from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def all_blogs(request):
    blogs = Blog.objects.order_by('-posted')
    return render(request, "blog/all_blogs.html", {"title": "All blogs", "blogs": blogs})

def detail(request, blog_id):
    # 1. You can redirecting to home page
    # try:
    #     blog = Blog.objects.get(pk=blog_id)
    # except:
    #     return redirect('home')

    # 2. Or write this:
    blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, "blog/detail_blog.html", {"title":f"Blog {blog_id}", "blog":blog})
