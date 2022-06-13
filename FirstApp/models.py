from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Emp(models.Model):
    empno = models.IntegerField(unique=True)
    ename = models.CharField(max_length=30)
    sal = models.IntegerField()
    deptno = models.IntegerField()

    def __str__(self):
        return str(self.empno)

class UserFormMy(models.Model):
    username = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username
class UserProfileInfo(models.Model):

    # Create relationship (don't inherit from User!)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add any additional attributes you want
    portfolio_site = models.URLField(blank=True)
    # pip install pillow to use this!
    # Optional: pip install pillow --global-option="build_ext" --global-option="--disable-jpeg"
    profile_pic = models.ImageField(upload_to='basic_app/profile_pics',blank=True)

    def __str__(self):
        # Built-in attribute of django.contrib.auth.models.User !
        return self.user.username