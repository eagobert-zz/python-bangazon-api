from rest_framework import serializers
from . models import Department, Computer, Training, Employee, Customer, PayType, PaymentType,ProductType, Product, ShoppingCart, Order

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ('department_name', 'budget')

class ComputerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computer
        fields = ('model_name', 'purchase_date', 'decommission_date')

class TrainingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Training
        fields = ('course_title', 'start_date', 'end_date', 'max_attendance')

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ('first_name', 'last_name', 'title', 'supervisor', 'department', 'computer', 'training')

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ('first_name', 'last_name', 'company_name', 'create_date', 'active')

class PayTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PayType
        fields = ('brand_name')

class PaymentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentType
        fields = ('account_number', 'pay_type', 'customer')

class ProductTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductType
        fields = ('type')

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_title', 'product_description', 'price', 'quantity', 'product_type', 'customer')

class ShoppingCartSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShoppingCart
        fields = ('product', 'quantity')

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('customer', 'payment_type', 'shopping_cart')