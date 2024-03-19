from django.db import models
# from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    id = models.BigAutoField(primary_key=True)
    pName = models.CharField(max_length=50, null=False, blank=False)
    desc = models.CharField(max_length=50,null=True,blank=True)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    createdTime=models.DateTimeField(auto_now_add=True)
    fields = {'pName', 'desc', 'price'}


    def __str__(self):
           return self.pName