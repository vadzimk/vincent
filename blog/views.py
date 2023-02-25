from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from blog.models import Post

class BlogListView(ListView):
    model = Post
    template_name = 'blog.html'
    context_object_name = 'all_blogs_list'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_content'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'blog_post_new.html'
    fields = ['title', 'author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog_post_edit.html'
    fields = ['title', 'body']