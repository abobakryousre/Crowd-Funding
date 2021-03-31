from django.db import models

from .projects import Project


class Images(modles.Model):
    path = models.ImageField()
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
        
    def __str__(self):
        return self.path
    