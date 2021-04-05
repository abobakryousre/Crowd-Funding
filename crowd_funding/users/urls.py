from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from users.views import index, display_category
urlpatterns = [
    path('', index),
    path('display-category/', display_category, name='display-category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
