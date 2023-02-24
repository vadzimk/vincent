from django.shortcuts import render
from django.views.generic import ListView

from posts.models import Post


class PostsPageView(ListView):
    model = Post
    template_name = 'posts.html'
    context_object_name = 'all_posts_list'