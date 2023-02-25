from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from blog.models import Post


class BlogTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret'
        )
        self.post = Post.objects.create(
            title='a good title',
            body='body content',
            author=self.user
        )

    def test_string_representation(self):
        post = Post(title='Sample title')
        self.assertEqual(str(post.title), post.title)

    def test_post_list_view(self):
        res = self.client.get(reverse('blogs'))
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "body content")
        self.assertTemplateUsed(res, 'blog.html')

    def test_post_detail_view(self):
        res = self.client.get('/blog/post/1/')
        self.assertEqual(res.status_code, 200)
        self.assertContains(res, "body content")
        self.assertTemplateUsed(res, 'post_detail.html')
        self.assertEqual(self.client.get('/blog/post/0/').status_code, 404)

    def test_post_create_view(self):
        res = self.client.post(reverse('post_new'), {
            'title': 'new title',
            'body': 'new text',
            'author': self.user.id
        })
        self.assertEqual(res.status_code, 302) # redirects to the newly created post
        self.assertEqual(Post.objects.last().title, 'new title')
        self.assertEqual(Post.objects.last().body, 'new text')

    def test_post_update_view(self):
        res = self.client.post(reverse('post_edit', args='1'), {
            'title': 'update title',
            'body': 'update body'
        })
        self.assertEqual(res.status_code, 302)
        self.assertEqual(Post.objects.get(id=1).title, 'update title')
        self.assertEqual(Post.objects.get(id=1).body, 'update body')

    def test_post_delete_view(self):
        res = self.client.post(reverse('post_delete', args='1'))
        self.assertEqual(res.status_code, 302)
        with self.assertRaises(Post.DoesNotExist):
            Post.objects.get(id=1)