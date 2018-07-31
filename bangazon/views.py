from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Customer, Product, PaymentType, Order, ProductType, Employee, Department, Computer, Training
from .serializers import CustomerSerializer, ProductSerializer, PaymentTypeSerializer, OrderSerializer, ProductTypeSerializer, EmployeeSerializer, DepartmentSerializer, ComputerSerializer, TrainingSerializer
import datetime


# Create your views here.
class CustomerViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT Customers """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post', 'put']
    
class ProductViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, DELETE Products """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class PaymentTypeViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, DELETE Payment Types """
    queryset = PaymentType.objects.all()
    serializer_class = PaymentTypeSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class OrderViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, DELETE Orders """
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class ProductTypeViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, DELETE Product Types """
    queryset = ProductType.objects.all()
    serializer_class = OrderSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class EmployeeViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT Employees """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    http_method_names = ['get', 'post', 'put']

class DepartmentViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT Departments """
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    http_method_names = ['get', 'post', 'put']

class ComputerViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, Delete Computers """
    queryset = Computer.objects.all()
    serializer_class = ComputerSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

class TrainingViewSet(viewsets.ModelViewSet):
    """ API endpoint to GET, POST, PUT, Delete Trainings """
    queryset = Training.objects.all()
    serializer_class = TrainingSerializer
    http_method_names = ['get', 'post', 'put', 'delete']

    def destroy(self, request, pk=None):
        """ Allows user to delete trainings greater than today's date"""
        if Training.start_date > datetime.date.today():
            instance = self.get_object()
            self.perform_destroy(instance)
            content = {'Method Not Allowed: Delete only future trainings'}
            return Response(content, status=status.HTTP_405_METHOD_NOT_ALLOWED)