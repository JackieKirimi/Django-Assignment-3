from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=200)
    population=models.IntegerField()
    area=models.FloatField()
    description=models.CharField(max_length=255)
    updated_at=models.DateTimeField(auto_now=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    

    def __str__(self):
        return self.name
    