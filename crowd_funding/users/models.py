from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    profile_picutre = models.ImageField(upload_to="users_images/", blank=True, null=True)
    mobile_phone = models.CharField(max_length=11)
    birth_date = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.first_name + self.last_name



