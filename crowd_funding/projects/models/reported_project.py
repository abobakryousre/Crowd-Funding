from django.db import models

from .projects import Projects

""" 
its work jsut like the  ReportedComment proccess, check it for more details
"""

class ReportedProject(models.Model):

    report_count = models.IntegerField(default=0)
    report_message = models.TextField()

    project = models.OneToOneField(
        Projects, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return "Project: " + self.project.title + " ,Report: " + self.report_message

    def incrementOne(self):
        self.report_count += 1
