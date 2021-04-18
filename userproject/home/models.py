from django.db import models

# Create your models here.

class AddUser(models.Model):
    name = models.CharField(max_length=122)
    age = models.IntegerField(max_length=2)
    sex = models.CharField(max_length=10)
    bloodgroup = models.CharField(max_length=3)
    email = models.CharField(max_length=122)
    phonenumber = models.IntegerField(max_length=12)
    address = models.TextField()
    date = models.DateField()
    def __str__(self):
        return self.name

class AddMedicine(models.Model):
    name = models.CharField(max_length=122)
    batch = models.CharField(max_length=20)
    manufacture = models.CharField(max_length=122)
    quantity = models.IntegerField()
    price = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return self.name