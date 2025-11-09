from django.urls import path
from . import views

urlpatterns = [
    path('employeeslist/', views.employee_list, name='employee_list'),
    path('employee/<int:employee_id>/', views.employee_detail, name='employee_detail'),
    path('engineers/', views.employee_enginerrs, name='employee_engineers'),
]