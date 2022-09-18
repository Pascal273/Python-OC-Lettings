from django.test import Client
from django.urls import reverse

import pytest


client = Client()


@pytest.mark.django_db
def test_index():

    title = bytes('<title>Lettings</title>', 'utf-8')

    url = reverse('lettings:index')
    response = client.get(url)
    print(response.content)
    assert response.status_code == 200
    assert title in response.content
