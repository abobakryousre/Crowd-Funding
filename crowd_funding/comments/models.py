from django.db import models
from projects.modles import Projects
from users.models import User

# Create your models here.

"""
 you should first to have a commint to report it,
 to check if the comment is reported or not use hasattr method -> hasattr(the objectInstance, 'reported_comment')

 to get ReportedComment object -> objectInstance.reportedcomment
 to get the report count  -> objectInstance.reportedcomment.report_count
 ************************************************************************
 # to create a reprot for some comment 
 report = ReportedComment.objects.create(comment=CommentobjectInstance)

 # to increment the report_count 
 #! note that you need the refernce of the  reported_comment instance to incremt it's count
 reprot_count = Comment.objects.filter('your conditino').reportedcomment
 report_count.incrementOne();

"""


class Comments(models.Model):
    message = models.CharField(max_length=150)
    # user has multiple comments
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    # project has multiple comments
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    def __str__(self):
        return self.message


class ReportedComment(models.Model):
    # the comment has only one reportedComment object
    report_count = models.IntegerField(default=1)
    comment = models.OneToOneField(
        Comments, on_delete=models.CASCADE, primary_key=True)

    def incrementOne(self):
        self.report_count+= 1
    def __str__(self):
        return str(self.report_count)
