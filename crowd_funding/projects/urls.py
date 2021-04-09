from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import createProject, projectDonate, index, project_details, report_project, rate_project

from .views import createProject, index, project_details, projectDonate, project_not_found

urlpatterns = [
    path('<int:id>', project_details, name="project_details"),
    path('create', createProject, name="create_project"),
    path('donate/<int:id>', projectDonate, name="donate_project"),
    path('index', index, name="projects_index"),
    path('<int:project_id>/report', report_project, name="report_project"),
    path('<int:project_id>/rate', rate_project, name="rate_project"),
    path('notfound', project_not_found, name="project_not_found"),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
