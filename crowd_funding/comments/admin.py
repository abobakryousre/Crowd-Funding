from django.contrib import admin, messages
from comments.models import Comments, ReportedComment

# Register your models here.
class CommentsAdmin(admin.ModelAdmin):

    def delete_comment(modeladmin, request, queryset):
        # check if the selected object is reported comment
        if hasattr(queryset[0], "report_count") and hasattr(queryset[0], "comment"):
            for reported_comment in queryset:
                comment = Comments.objects.get(pk=reported_comment.comment.id)
                comment.delete()
            messages.success(request, "Selected Comment(s) Deleted Successfully")
        else:
            messages.error(request, "The is not a Reported Comment")
    admin.site.add_action(delete_comment, "Delete Reported Comment")


admin.site.register(Comments, CommentsAdmin)
admin.site.register(ReportedComment)
