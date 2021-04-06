from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path

from .views import (change_password, check_password, delete_account,
                    deleteItem, edit_profile, index, view_profile)

urlpatterns = [
    path('', index, name="index"),
    path("profile/edit", edit_profile, name="edit-profile"),
    path("profile/", view_profile, name="profile"),
    path('profile/check-password', check_password, name="check-password"),
    path('delete-account/', delete_account, name='delete-account'),
    path('profile/change-password', change_password, name='change-password'),
    url(r'^deleteItem/(?P<pk>\d+)$', deleteItem,name='deleteItem'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
