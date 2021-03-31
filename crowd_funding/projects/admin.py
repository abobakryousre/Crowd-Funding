from django.contrib import admin
from projects.models import Projects
from comments.models import Comments
# Register your models here.

admin.site.register(Projects)
admin.site.register(Comments)