from django.db import models

# Create your models here.
class Employees(models.Model):
    name=models.CharField(max_length=50, blank=False, null=False)
    email=models.EmailField()
    position=models.CharField(max_length=50, blank=False, null=False)
    age=models.IntegerField()
    gender=models.CharField(max_length=25, blank=False, null=False)
    department=models.CharField(max_length=100, blank=False, null=False)
    salary=models.IntegerField(blank=False, null=False)

    
    def __str__(self) :
        return self.name