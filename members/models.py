from django.db import models

class Members(models.Model):
    fname=models.CharField(max_length=50)
    lname=models.CharField(max_length=50)
