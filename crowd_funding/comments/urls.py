from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import report_comment

app_name = "comments"
urlpatterns = [
    path('<int:comment_id>/report', report_comment, name="report_comment"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
