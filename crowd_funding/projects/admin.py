from django.contrib import admin
from projects.models import Projects
from comments.models import Comments
from projects.models.projects import Category
from projects.models import Images
# Register your models here.

admin.site.register(Projects)
admin.site.register(Comments)
admin.site.register(Category)
admin.site.register(Images)