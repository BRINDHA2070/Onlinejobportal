from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Recruiter(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.IntegerField(null=True)
    image = models.FileField(null=True)
    company= models.CharField(max_length=100,null=True)
    gender= models.CharField(max_length=100,null=True)
    type=models.CharField(max_length=100,null=True)
    status=models.CharField(max_length=100,null=True)
    def _str_(self):
        return self.user.username
		
		
class SignupUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    mobile = models.IntegerField(null=True)
    image = models.FileField(null=True)
    gender= models.CharField(max_length=100,null=True)
    type=models.CharField(max_length=100,null=True)
    def _str_(self):
        return self.user.username
		
class Add_job(models.Model):
    recruiter = models.ForeignKey(Recruiter,on_delete=models.CASCADE,null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    title = models.CharField(max_length=30,null=True)
    position = models.CharField(max_length=30,null=True)
    image = models.FileField(null=True)
    description = models.CharField(max_length=30,null=True)
    experience = models.CharField(max_length=30,null=True)
    location = models.CharField(max_length=30,null=True)
    skills = models.CharField(max_length=30,null=True)
    def __str__(self):
        return self.title+" "+self.recruiter.company
		
class Apply(models.Model):
    job=models.ForeignKey(Add_job,on_delete=models.CASCADE,null=True)
    sign=models.ForeignKey(SignupUser,on_delete=models.CASCADE,null=True)
    image = models.FileField(null=True)
    def __str__(self):
        return self.sign.user.username+" "+self.job.title

class Send_Feedback(models.Model):
    profile = models.ForeignKey( Recruiter, on_delete=models.CASCADE, null=True)
    message1 = models.TextField(null=True)
    date = models.CharField(max_length=30, null=True)


