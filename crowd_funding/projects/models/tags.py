from django.db import models

from .projects import Project


class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.tag_name

