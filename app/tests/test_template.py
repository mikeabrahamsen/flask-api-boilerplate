from unittest import TestCase
from app import app, main


class TemplateTests(TestCase):
    def setUp(self):
        self.test_app = app.test_client()

    def tearDown(self):
        pass

    def check_content_type(self, headers):
        self.assertEqual(headers['Content-Type'], 'application/json')
