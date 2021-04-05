from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import report_comment

urlpatterns = [
    path('/projects/<int:project_id>/comments/<int:comment_id>/report', report_comment, name="project_details"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
