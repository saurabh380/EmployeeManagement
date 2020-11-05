from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save,post_save
import datetime

# Create your models here.
class emplyee_details(models.Model):
    mobile = models.PositiveIntegerField(blank=True,null=True)
    dob = models.DateField(null= True,blank=True)
    current_profile = models.CharField(max_length=20,null= True,blank=True)
    degination = models.CharField(max_length = 20,null= True,blank=True)
    resume = models.FileField(upload_to='uploads/', blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE,related_name='emp',)

class leave_request(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    duration_from = models.DateField()
    duration_to = models.DateField()
    leave_msg = models.TextField()


def create_profile(sender,instance,created,**kwargs):
    if created:
        emplyee_details.objects.create(user=instance)
post_save.connect(create_profile, sender=User)


