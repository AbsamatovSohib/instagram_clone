from django.test import TestCase
from django.http import HttpRequest
from insta.views import home_page
# Create your tests here.


class HomePageTest(TestCase):
    def tests(self):
        request = HttpRequest()
        response = home_page(request)

        html = response.content.decode("utf8")
        self.assertIn("<title>To-Do lists</title>", html)
        self.assertTrue(html.startswith("<html>"))
        self.assertTrue(html.endswith("</html>"))

