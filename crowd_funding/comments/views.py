from django.shortcuts import render
from projects.models import Projects
from .models import Comments, ReportedComment

# Create your views here.

def report_comment(request, project_id, comment_id):
    project = Projects.objects.get(id=project_id)
    comment = Comments.objects.filter(project=project).get(id=comment_id)

    return render(request, 'report_comment.html', {"comment": comment})
