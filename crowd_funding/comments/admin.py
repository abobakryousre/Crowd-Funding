from django.contrib import admin
from comments.models import Comments, ReportedComment

# Register your models here.
admin.site.register(Comments)
admin.site.register(ReportedComment)
