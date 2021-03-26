from django.db import models

class User(models.Model):
    name = models.CharField(max_length = 20)
    phoneNumber = models.IntegerField(default = 9999999999)
    password = models.CharField(max_length = 20)
    dateOfBirth = models.CharField(max_length = 10)
