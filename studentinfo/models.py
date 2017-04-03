from __future__ import unicode_literals
from time import time
from django.db import models

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

class Student(models.Model):
    name = models.CharField(max_length=500)
    father_name = models.CharField(max_length=500)
    mother_name = models.CharField(max_length=500)
    registration_no = models.CharField(max_length=200)
    dept = models.CharField(max_length=500)
    semester = models.IntegerField(default=1)
    branch = models.CharField(max_length=500)
    #email = models.EmailField()
    thumbnail = models.FileField(upload_to=get_upload_file_name)
