from django.contrib import admin
from empApp.models import Employee
# Register your models here.
#to create better ui of admin portal
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['firstName','lastName']

admin.site.register(Employee,EmployeeAdmin)
