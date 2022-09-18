from django.test import TestCase
from django.urls import reverse

from .models import Address, Letting


class TestLettingsViews(TestCase):

    def setUp(self):
        """Create required objects for the test database"""
        self.address = Address.objects.create(
            number=4,
            street='Military Street',
            city='Willoughby',
            state='OH',
            zip_code=44094,
            country_iso_code='USA'
        )
        self.letting = Letting.objects.create(
            title='Oceanview Retreat',
            address=self.address
        )

    def test_index(self):
        """Test If the correct title is in the response"""
        wanted_title = bytes('<title>Lettings</title>', 'utf-8')
        url = reverse('lettings:index')
        response = self.client.get(url)
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )

    def test_letting(self):
        """Test If the correct title is in the response"""
        letting = self.letting  # get test-letting
        wanted_string = f'<title>{letting.title}</title>'  # create wanted title tag
        wanted_title = bytes(wanted_string, 'utf-8')  # format title tag into bytes

        url = reverse('lettings:letting', kwargs={'letting_id': 1})  # get URL
        response = self.client.get(url)  # get response

        # check if wanted title is title of response
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )
