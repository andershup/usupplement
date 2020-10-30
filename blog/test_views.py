from django.test import TestCase
from .models import Post
# Create your tests here.

class TestViews(TestCase):
    """def test_get_add_blog_page(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/add_blog.html')"""

    def test_can_add_item(self):
        response = self.client.post('/')
