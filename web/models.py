from django.db import models
import uuid
from datetime import datetime
def generate_8_digit_id():
    return int(str(uuid.uuid1().int)[-8:])

class Quotation(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=150)
    Phone = models.CharField(max_length=25)
    Looking = models.CharField(max_length=50)
    Status  = models.BooleanField(default=False)
    Budget = models.IntegerField()
    def __str__(self):
        return str(self.Name)

class Blog(models.Model):
    Title =  models.CharField(max_length=50)
    Description = models.CharField(max_length=200)
    Link = models.URLField()
    def __str__(self):
        return str(self.Title)

class Project(models.Model):
    Title =  models.CharField(max_length=50)

    Category= models.CharField(max_length=50)
    Color = models.CharField(max_length=8)
    Image =  models.ImageField(upload_to="projects")
    Link = models.URLField()
    def __str__(self):
        return str(self.Title)


class Service_No(models.Model):
    id = models.BigAutoField(primary_key=True, default=generate_8_digit_id)
    password = models.CharField(max_length=50)
    name =  models.CharField(max_length=50)
    def __str__(self):
        return str(self.id)

class Service(models.Model):
    service_no =  models.ForeignKey(Service_No , on_delete=models.CASCADE)
    Title =  models.CharField(max_length=400)
    Date = models.DateField(null=True)
    Description = models.CharField(max_length=300,blank=True)
    Link = models.URLField()


class Cosultation(models.Model):
    Name = models.CharField(max_length=50)
    Email = models.CharField(max_length=150)
    Phone = models.CharField(max_length=150)
    
    Date_Time = models.DateTimeField()

    def __str__(self):
        return str(self.Date_Time)

