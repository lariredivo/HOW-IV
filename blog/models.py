from django.db import models


class Assist(models.Model):
    name = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11)
    telephone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
