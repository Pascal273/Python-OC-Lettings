from django.contrib import admin
from django.urls import path, include

from . import views
import lettings.urls
import profiles.urls


urlpatterns = [
    path('', views.index, name='index'),
    path('', include((lettings.urls, 'lettings'), namespace='lettings')),
    path('', include((profiles.urls, 'profiles'), namespace='profiles')),
    path('admin/', admin.site.urls),
]
