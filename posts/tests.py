from django.test import TestCase
from django.urls import reverse

from posts.models import Post


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text='just a test')

    def test_text_content(self): # this is actually testing the setUp method
        post = Post.objects.get(id=1)
        self.assertEqual(post.text, 'just a test')


class HomePageViewTest(TestCase):
    def setUp(self):
        Post.objects.create(text='this is another test')

    def test_view_url_exists_at_proper_location(self):
        res = self.client.get('/posts/')
        self.assertEqual(res.status_code, 200)

    def test_view_url_by_name(self):
        # print(f"->{reverse('posts')}<-")
        res = self.client.get(reverse('posts'))
        self.assertEqual(res.status_code, 200)
        self.assertTemplateUsed(res, 'posts.html')