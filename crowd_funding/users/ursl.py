from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import index, edit_profile, view_profile, check_password, delete_account
urlpatterns = [
    path('', index, name="index"),
    path("profile/edit", edit_profile, name="edit-profile"),
    path("profile/", view_profile, name="profile"),
    path('profile/check-password', check_password, name="check-password"),
    path('delete-account/', delete_account, name='delete-account'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
