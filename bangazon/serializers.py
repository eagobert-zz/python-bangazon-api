from rest_framework import serializers
from . import models


class DepartmentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Department
        fields = ('id','url','department_name', 'budget')

class ComputerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Computer
        fields = ('id','url','model_name', 'purchase_date', 'decommission_date')

class TrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Training
        fields = ('id','url','course_title', 'start_date', 'end_date', 'max_attendance')

class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    # training = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = models.Employee
        fields = ('id','url','first_name', 'last_name', 'title', 'supervisor', 'department', 'computer', 'training')

class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id','url','first_name', 'last_name', 'company_name', 'create_date', 'active')

class PayTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PayType
        fields = ('id','url','brand_name')

class PaymentTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.PaymentType
        fields = ('id','url','account_number', 'pay_type', 'customer')

class ProductTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.ProductType
        fields = ('id','url','type')

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Product
        fields = ('id','url','product_title', 'product_description', 'price', 'quantity', 'product_type', 'customer')

class OrderProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.OrderProduct
        fields = ('id','url','product', 'order')

class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id','url','customer', 'payment_type', 'shopping_cart')

class EmployeeTrainingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.EmployeeTraining
        fields = ('id','url','employee', 'training')
