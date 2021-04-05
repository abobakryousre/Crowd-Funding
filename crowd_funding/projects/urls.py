from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from .views import createProject, projectDonate, index, project_details

urlpatterns = [
    path('<int:id>', project_details, name="project_details"),
    path('create', createProject, name="create_project"),
    path('donate/<int:id>', projectDonate, name="donate_project"),
     path('index', index, name="projects_index"),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
