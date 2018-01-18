from django.test import TestCase, Client
from django.urls import reverse


class PortalTests(TestCase):
    def setUp(self):
        self.c = Client()

    def test_home(self):
        response = self.c.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
