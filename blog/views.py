from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post
# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'all_blogs_list'


class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_content'