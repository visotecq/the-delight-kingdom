from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=120,unique=True)
    description = models.TextField()
    image_url = models.FileField(upload_to='uploads/')
    active = models.BooleanField(default=False)

    def __str__(self):
        return '%s' % (self.name)
    
class Product(models.Model):
    name = models.CharField(max_length=120)
    description = models.TextField()
    quantity = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE,blank=True,null=True)
    image_url = models.FileField(upload_to='uploads/')
    active = models.BooleanField(default=False)

    def _str_(self):
        return self.name
    
