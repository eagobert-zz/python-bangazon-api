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
    training = models.ManyToManyField(Training)

    def __str__(self):
        return "Employee Name: {0} {1}, Title: {2}, Department: {3}".format(self.first_name, self.last_name, self.title, self.department)

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
        return f"Customer Name: {self.first_name} {self.last_name}, Company: {self.company_name}"

class PayType(models.Model):
    """ Model represents the name of a payment type """
    brand_name = models.CharField(max_length=15)

    def __str__(self):
        return "Pay Type: %s" % self.brand_name

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
        return "Customer's Payment Type: %s" % self.account_number

class ProductType(models.Model):
    """ Model represents a product type """
    type = models.CharField(max_length=15)

    def __str__(self):
        return "Product Type: %s" % self.type

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
        return f"Product Title: {self.product_title}, Seller: {self.customer}, Quantity Available: {self.quantity}"

class ShoppingCart(models.Model):
    """ Model represents a shopping cart of products """
    product = models.ForeignKey(
        Product,
        on_delete = models.CASCADE
        )
    quantity = models.SmallIntegerField()

    def __str__(self):
        return f"Added to Cart: {Product.product_title}, price {Product.price}, items {self.quantity}"

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
    shopping_cart = models.OneToOneField(
        ShoppingCart,
        on_delete=models.CASCADE
        )

    def __str__(self):
        return f"Customer Name: {Customer.first_name} {Customer.last_name}, Company: {Customer.company_name}, Payment Type: {PayType.brand_name}"
