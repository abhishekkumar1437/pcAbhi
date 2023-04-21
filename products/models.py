
from django.db import models



# Create your models here.
class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    
    def __str__(self):
        return self.title

class image(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    price=models.IntegerField()
    image=models.ImageField(upload_to='images')
    cate=models.ForeignKey(Category,on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.title
    
class Order(models.Model):
    name=models.CharField(max_length=100)
    amount=models.IntegerField()
    
  


