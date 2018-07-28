from django.db import models
from datetime import date

# Create your models here.
class Department(models.Model):
    department_name = models.CharField(max_length=30)
    budget = models.DecimalField(max_digits=None, decimal_places=2)

class Computer(models.Model):
    purchase_date = models.DateField()
    decommission_date = models.DateField()

class Employee(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    supervisor = models.BooleanField(default=False)
    department = models.OneToOneField(
        Department, 
        on_delete=models.CASCADE
        )
    computer = models.OneToOneField(
        Computer,
        on_delete=models.CASCADE
        )
