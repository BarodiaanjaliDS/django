from django.shortcuts import render
from .models import Employee, Department, Role

# Create your views here.
def index(request):
    return render(request, 'index.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    return render(request, 'view_all_emp.html', context)

def add_emp(request):
    return render(request, 'add_emp.html')

def remove_emp(request):
    return render(request, 'remove_emp.html')

def filter_emp(request):
    return render(request, 'filter_emp.html')

