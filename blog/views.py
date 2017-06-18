# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Blog
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def blog_title(request):
    blogs = Blog.objects.all()
    return render(request,"blog/title.html",{"blogs":blogs})
@login_required
def blog_body(request,blog_id):
    blog = Blog.objects.get(id=blog_id)
    return render(request,"blog/body.html",{"blog":blog})
