from django.db import models

from .projects import Projects
from users.models import User

""" 
its work jsut like the  ReportedComment proccess, check it for more details
"""

class ReportedProject(models.Model):

    report_count = models.IntegerField(default=0)

    project = models.OneToOneField(
        Projects, on_delete=models.CASCADE)

    def __str__(self):
        return "Project: " + self.project.title + ", Report Count: " + str(self.report_count)

    def incrementOne(self):
        self.report_count += 1


class Report(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    report_message = models.TextField()

    def __str__(self):
        return "Project: " + self.project.title + ", User: " + self.user.email
