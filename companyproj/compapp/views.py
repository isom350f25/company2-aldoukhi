from django.shortcuts import render
from .models import Employee , project
from django.utils import timezone
# Create your views here.

def employee_list(request):
    employees = Employee.objects.all().order_by('name')
    return render(request, 'employee_list.html', {'employees': employees})

def employee_detail(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    today = timezone.now().date()
    projects = employee.projects.filter(start_date__lte=today, end_date__gte=today)
    return render(request, 'employee_detail.html', {'employee': employee , 'projects':projects})    

def employee_enginerrs(request):
    employees = Employee.objects.filter(position__icontains='Engineer')
    return render(request, 'employee_list.html', {'employees': employees})

