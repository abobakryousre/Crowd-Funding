from django.db import models

from .projects import Projects

""" 
check the __init__ file for more details !
"""


class Rating(models.Model):
    one_star = models.IntegerField(default=0)
    two_star = models.IntegerField(default=0)
    three_star = models.IntegerField(default=0)
    four_star = models.IntegerField(default=0)
    five_star = models.IntegerField(default=0)
    #projcet mas many rating
    project = models.OneToOneField(Projects, on_delete=models.CASCADE, primary_key=True)

    def getAvarageStar(self):
        return (self.one_star + self.two_star + self.three_star + self.four_star + self.five_star ) / 5
    def __str__(self):
        return self.project.title