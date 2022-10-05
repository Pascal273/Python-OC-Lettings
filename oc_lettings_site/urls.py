from django.contrib import admin
from django.urls import path, include

from . import views
import lettings.urls
import profiles.urls


# Sentry test function that causes an error
def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('', include((lettings.urls, 'lettings'), namespace='lettings')),
    path('', include((profiles.urls, 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
    path('sentry-debug/', trigger_error),  # Sentry test url
]
