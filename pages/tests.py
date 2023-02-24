from django.test import TestCase


class SimpleTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        self.assertEqual(self.client.get('/about/').status_code, 200)  # if  no trailing '/' will be status 301
