from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    subject = models.TextField(max_length=1000)
    desc = models.TextField(max_length=1000)
    date = models.DateField()

    def __str__(self):
      return self.name


class Mssg(models.Model):
    name = models.CharField(max_length=122)
    mobile = models.IntegerField()
    purpose = models.CharField(max_length=122)

    def __str__(self):
       return self.name
    

class add_Blog(models.Model):
   tit=models.CharField(max_length=50)
   category=models.CharField(max_length=50)
   content=models.CharField(max_length=1100)
   summary=models.CharField(max_length=1200)
   image=models.ImageField(upload_to="static/images")

   def __str__(self):
      return self.name
   
      
   
   
   
     
