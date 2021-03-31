from django.db import models

from .projects import Projects

""" 
check the __init__ file for more details !
"""


class Images(models.Model):
    path = models.ImageField(upload_to="projects_images/", blank=True, null=True)
    #project has many images
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def __str__(self):
        return self.path
    