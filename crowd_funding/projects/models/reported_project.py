from django.db import models

from .projects import Projects

""" 
its work jsut like the  ReportedComment proccess, check it for more details
"""

class ReportedProject(models.Model):

    report_count = models.IntegerField(default=0)

    project = models.OneToOneField(
        Project, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.report_count)

    def incrementOne(self):
        self.report_count+= 1
