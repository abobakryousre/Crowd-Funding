from django.db import models


class Projects(models.Model):
    title = models.CharField(max_length=50, null=False)
    details = models.CharField(max_length=250)
    category = models.CharField(max_length=50)
    total_target = models.IntegerField(null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    start_time = models.DateField(auto_now=False, auto_now_add=False, null=False)
    end_time = models.DateField(auto_now=False, auto_now_add=False, null=False)

    def __str__(self):
        return self.title

    