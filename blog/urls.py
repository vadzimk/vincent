from django.urls import path
from .views import BlogListView, BlogDetailView

urlpatterns = [
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'), # pk is a url parameter that is passed to the post_detail in the template
    path('', BlogListView.as_view(), name='blogs'),  # root of 'blog/'
]
