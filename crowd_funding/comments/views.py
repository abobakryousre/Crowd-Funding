import json

from django.shortcuts import render
from projects.models import Projects
from .models import Comments, ReportedComment
from django.http import HttpResponse


# Create your views here.

def report_comment(request, project_id, comment_id):
    project = Projects.objects.get(id=project_id)
    comment = Comments.objects.filter(project=project).get(id=comment_id)
    if request.method == 'POST':
        report_message = request.POST.get('report')

        response_data = {}
        ReportedComment.objects.create(comment=comment, report_message=report_message)

        response_data['result'] = "report successful"
        response_data['comment_id'] = comment.id

        return HttpResponse(json.dumps(response_data), content_type="application/json")
    return HttpResponse("Reported")
