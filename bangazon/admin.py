from django.contrib import admin
from . import models
# from . models import Department, Computer, Training, Employee, Customer, PayType, PaymentType, ProductType, Product, ShoppingCart, Order


# Register your models here.
admin.site.register(models.Customer)
admin.site.register(models.Computer)
admin.site.register(models.Training)
admin.site.register(models.Employee)
admin.site.register(models.Department)
admin.site.register(models.PayType)
admin.site.register(models.PaymentType)
admin.site.register(models.ProductType)
admin.site.register(models.Product)
admin.site.register(models.OrderProduct)
admin.site.register(models.Order)
admin.site.register(models.EmployeeTraining)
