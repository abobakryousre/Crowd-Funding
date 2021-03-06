from django.db import models
from users.models import User

"""  
#to get all the project comments 
your projectInstanc.comments_set.all()
"""

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name



class Projects(models.Model):
    title = models.CharField(max_length=50, null=False)
    details = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    total_target = models.FloatField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateField(auto_now=False, auto_now_add=False, null=False)
    end_time = models.DateField(auto_now=False, auto_now_add=False, null=False)
    selected = models.BooleanField(default=False)
    # user has multiple projects
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Donation(models.Model):

    amount = models.FloatField(null=False)
    #user can donate many time
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # project has many donation
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    

    def __str__(self):
        return str(self.name)


