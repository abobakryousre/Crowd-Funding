from django.db import models

from .projects import Projects

""" 
check the __init__ file for more details !
"""

class Tags(models.Model):
    tag_name = models.CharField(max_length=50)
    #project has many tags
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    def __str__(self):
        return self.tag_name

