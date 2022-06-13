from django.db import models
from django.contrib.auth.models import User
import datetime
import os
# Create your models here.

def filepath(request, filename):
    old_filename = filename
    timeNow = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (timeNow, old_filename)
    return os.path.join('static/images', filename)

class Add(models.Model):
    Username = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    profession = models.CharField(max_length=50, null=True)
    description = models.TextField(max_length=500, null=True)
    image = models.ImageField(default="no-image.jpg",upload_to=filepath, null=True, blank=True)