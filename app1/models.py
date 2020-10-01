from django.db import models

class user(models.Model):
    name = models.CharField(max_length=80)
    contact = models.IntegerField()
    password=models.CharField(max_length=40)
    username= models.CharField(max_length=20)
    email=models.CharField(max_length=20)


