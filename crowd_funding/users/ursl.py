from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, edit_profile
urlpatterns = [
    path('', index, name="index"),
    path("profile/edit", edit_profile, name="edit-profile"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
