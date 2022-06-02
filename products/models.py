from django.db import models

class Entries(models.Model):
    name=models.CharField(max_length=100,null=False)
    price=models.IntegerField(null=False)
    type=models.CharField(max_length=100,null=False)
    description=models.CharField(max_length=150,null=False)
    
