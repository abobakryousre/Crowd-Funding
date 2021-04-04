from django.contrib import admin
from projects.models import Projects, Rating, Tags, Images, ReportedProject
from comments.models import Comments, ReportedComment

# Register your models here.

admin.site.register(Projects)
admin.site.register(Rating)
admin.site.register(Tags)
admin.site.register(Images)
admin.site.register(ReportedProject)
admin.site.register(Comments)
admin.site.register(ReportedComment)
