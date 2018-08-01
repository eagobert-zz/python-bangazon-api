from django.conf.urls import url, include
from rest_framework import routers
from . import views


#Register routes here:
router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('products', views.ProductViewSet)
router.register('paymenttypes', views.PaymentTypeViewSet)
router.register('orders', views.OrderViewSet)
router.register('producttypes', views.ProductTypeViewSet)
router.register('employees', views.EmployeeViewSet)
router.register('departments', views.DepartmentViewSet)
router.register('computers', views.ComputerViewSet)
router.register('trainings', views.TrainingViewSet)
router.register('orderproducts', views.OrderProductViewSet)
router.register('employeetrainings', views.EmployeeTrainingViewSet)

urlpatterns = [
    url('', include(router.urls))
]
