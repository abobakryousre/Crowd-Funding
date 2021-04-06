from django.contrib import admin
from projects.models import Projects, Tags
from projects.models.projects import Category
from projects.models import Images
from projects.models.reported_project import ReportedProject
# Register your models here.

admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(ReportedProject)
