from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True,default=True)
    blog_title=models.CharField(max_length=100000)
    blog_description=models.TextField()
    blog_image=models.ImageField(upload_to="blogs/")
    pub_date = models.DateTimeField(default=datetime.now,blank=True)