from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView

urlpatterns = [
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'),
    path('post/new/', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # pk is a url parameter that is passed to the post_detail in the template
    path('', BlogListView.as_view(), name='blogs'),  # root of 'blog/'
]
