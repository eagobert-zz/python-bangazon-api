from django.contrib import admin
from . models import Department, Computer, Training, Employee, Customer, PayType, ProductType, Product, ShoppingCart, Order


# Register your models here.
admin.site.register(Department)
admin.site.register(Computer)
admin.site.register(Training)
admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(PayType)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(ShoppingCart)
admin.site.register(Order)
