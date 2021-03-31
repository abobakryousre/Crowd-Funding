from django.db import models

# Create your models here.

"""
 you should first to have a commint to report it,
 to check if the comment is reported or not use hasattr method -> hasattr(the objectInstance, 'reported_comment')

 to get reportedComment -> objectInstance.reported_comment


"""


class Comments(models.Model):
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.message


class ReportedComment(models.Model):
    # the comment has only one reportedComment object
    report_count = models.IntegerField()
    comment = models.OneToOneField(
        Comments, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.report_count
