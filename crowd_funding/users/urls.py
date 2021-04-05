from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import index, display_category, search_for_projects
urlpatterns = [
    path('', index),
    path('display-category/', display_category, name='display-category'),
    path('search-for-projects', search_for_projects, name='search-for-projects'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
