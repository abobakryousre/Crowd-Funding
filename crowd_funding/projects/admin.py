from comments.models import Comments, ReportedComment
from django.contrib import admin

from projects.models import Images, Projects, Rating, ReportedProject, Tags

# Register your models here.

admin.site.register(Projects)
admin.site.register(Rating)
admin.site.register(Tags)
admin.site.register(Images)
admin.site.register(ReportedProject)
admin.site.register(Comments)
admin.site.register(ReportedComment)
from comments.models import Comments

from projects.models import Images, Projects
from projects.models.projects import Category

# Register your models here.

admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Images)
