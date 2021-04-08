from django.contrib import admin
from projects.models import Projects, Tags, Rating
from projects.models.projects import Category
from projects.models import Images
from projects.models.reported_project import ReportedProject, Report
from projects.models.rating import Rate
from django.contrib import admin, messages


# Register your models here.
class ReportedProjectAdmin(admin.ModelAdmin):
    def delete_project(modeladmin, request, queryset):
        # check if the select object is project
        if hasattr(queryset[0], "report_count") and hasattr(queryset[0], "project"):
            for reported_project in queryset:
                project = Projects.objects.get(pk=reported_project.project.id)
                project.delete()
            messages.success(request, "Selected Project(s) Deleted Successfully")
        else:
            messages.error(request, "This is not a Reported Project")

    admin.site.add_action(delete_project, "Delete Reported Project")


admin.site.register(ReportedProject, ReportedProjectAdmin)
admin.site.register(Projects)
admin.site.register(Category)
admin.site.register(Images)
admin.site.register(Tags)
admin.site.register(Report)
admin.site.register(Rating)
admin.site.register(Rate)
