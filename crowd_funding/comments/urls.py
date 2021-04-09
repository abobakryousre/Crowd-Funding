from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import report_comment, delete_comment

app_name = "comments"
urlpatterns = [
    path('<int:comment_id>/report', report_comment, name="report_comment"),
    path('<int:comment_id>/delete', delete_comment, name="delete_comment"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
