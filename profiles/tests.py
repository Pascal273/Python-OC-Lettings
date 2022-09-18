from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Profile


User = get_user_model()


class TestProfilesViews(TestCase):

    def setUp(self):
        """Create required objects for the test database"""
        self.user = User.objects.create(
            username='HeadlinesGazer',
            first_name='Jamie',
            last_name='Lal',
            email='jssssss33@acee9.live',
            password='mnfgjfnlgjk12-R'
        )
        self.profile = Profile.objects.create(
            user=self.user,
            favorite_city='Buenos Aires'
        )

    def test_index(self):
        """Test If the correct title is in the response"""
        wanted_title = bytes('<title>Profiles</title>', 'utf-8')  # format title tag in bytes
        url = reverse('profiles:index')  # get url
        response = self.client.get(url)  # get response

        # check if wanted title is title of response
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )

    def test_profile(self):
        """Test If the correct title is in the response"""
        profile = self.profile  # get test-profile
        wanted_string = f'<title>{profile.user.username}</title>'  # create wanted title tag
        wanted_title = bytes(wanted_string, 'utf-8')  # format title tag into bytes

        url = reverse('profiles:profile', kwargs={'username': profile.user.username})  # get URL
        response = self.client.get(url)  # get response

        # check if wanted title is title of response
        self.assertIn(
            member=wanted_title,
            container=response.content,
            msg='Title not in response!'
        )
