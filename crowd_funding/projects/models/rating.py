from django.db import models

from .projects import Projects

""" 
check the __init__ file for more details !
"""


class Rating(models.Model):
    one_star = models.IntegerField(default=0, null=True, blank=True)
    two_star = models.IntegerField(default=0, null=True, blank=True)
    three_star = models.IntegerField(default=0, null=True, blank=True)
    four_star = models.IntegerField(default=0, null=True, blank=True)
    five_star = models.IntegerField(default=0, null=True, blank=True)
    #projcet mas many rating
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)

    def get_average_rating(self):
        return (self.one_star + self.two_star + self.three_star + self.four_star + self.five_star ) / 5
