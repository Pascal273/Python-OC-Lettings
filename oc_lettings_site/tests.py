from django.test import SimpleTestCase
from django.urls import reverse


class TestIndex(SimpleTestCase):

    def test_index(self):
        wanted_title = bytes('<title>Holiday Homes</title>', 'utf-8')
        url = reverse('index')
        response = self.client.get(url)
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )
