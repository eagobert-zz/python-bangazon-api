from django.db import models
from datetime import date


# Create your models here.
class Department(models.Model):
    """ Model represents an employee department """
    department_name = models.CharField(max_length=30)
    budget = models.DecimalField(max_digits=20, decimal_places=2)

    def __str__(self):
        return "Department: %s" % self.department_name

class Computer(models.Model):
    """ Model represents an employee computer """
    model_name = models.CharField(max_length=30, null=True)
    purchase_date = models.DateField()
    decommission_date = models.DateField()

    def __str__(self):
        return "Computer: %s" % self.model_name

class Training(models.Model):
    """ Model represents a training course """
    course_title = models.CharField(max_length=30)
    start_date = models.DateField()
    end_date = models.DateField()
    max_attendance = models.IntegerField()

    def __str__(self):
        return "Training Name: %s" % self.course_title

class Employee(models.Model):
    """ Model represents an employee """
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
    training = models.ManyToManyField(
        Training,
        through='EmployeeTraining')

    def __str__(self):
        return "Employee Name: {0} {1}, Title: {2}, Department: {3}".format(self.first_name, self.last_name, self.title, self.department)

class EmployeeTraining(models.Model):
    """ Model represents employee training"""
    employee = models.ForeignKey(
        Employee,
        on_delete = models.CASCADE
        )
    training = models.ForeignKey(
        Training,
        on_delete = models.CASCADE
        )

class Customer(models.Model):
    """ Model represents a customer """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    company_name = models.CharField(
        max_length=30,
        blank=True
        )
    create_date = models.DateField()
    active = models.BooleanField(default=True)

    def __str__(self):
        if self.company_name == '':
            return f"{self.first_name} {self.last_name}"
        else:
            return f"{self.company_name}"

class PayType(models.Model):
    """ Model represents the name of a payment type """
    brand_name = models.CharField(max_length=15)

    def __str__(self):
        return self.brand_name

class PaymentType(models.Model):
    """ Model represents a customer payment account """
    account_number = models.IntegerField()
    pay_type = models.OneToOneField(
        PayType,
        on_delete = models.CASCADE
        )
    customer = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE
        )

    def __str__(self):
        return self.account_number

class ProductType(models.Model):
    """ Model represents a product type """
    type = models.CharField(max_length=15)

    def __str__(self):
        return self.type

class Product(models.Model):
    """ Model represents a product """
    product_title = models.CharField(max_length=30)
    product_description = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    quantity = models.SmallIntegerField()
    product_type = models.OneToOneField(
        ProductType,
        on_delete = models.CASCADE
        )
    customer = models.ForeignKey(
        Customer,
        on_delete = models.CASCADE
        )
    
    def __str__(self):
        return f"{self.product_title}"


class Order(models.Model):
    """ Model represents a customer's order """
    customer = models.OneToOneField(
        Customer, 
        on_delete=models.CASCADE
        )
    payment_type = models.ForeignKey(
        PaymentType,
        on_delete=models.CASCADE,
        blank=True
        )
    product = models.ManyToManyField(
        Product,
        through='OrderProduct'
        )

    def __str__(self):
        return f"Customer Name: {Customer.first_name} {Customer.last_name}, Company: {Customer.company_name}, Payment Type: {PayType.brand_name}"

class OrderProduct(models.Model):
    """ Model represents a line items in an order """
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
        )
    order = models.ForeignKey(
        Order,
        on_delete = models.CASCADE
    )
