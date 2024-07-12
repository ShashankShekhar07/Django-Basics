from django.shortcuts import render
from empApp.models import Employee

# Create your views here.
def employeedata(request):
    employees=Employee.objects.all() #take models
    empDict = {'employees':employees}
    return render(request,'employees.html',empDict)
