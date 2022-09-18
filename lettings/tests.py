from django.test import TestCase
from django.urls import reverse


class TestIndex(TestCase):

    def test_index(self):
        wanted_title = bytes('<title>Lettings</title>', 'utf-8')
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )
