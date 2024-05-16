from django.contrib import admin
from .models import Employee , Contractor , Manager 

@admin.register(Employee)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Age' , 'Salary','hours']

@admin.register(Contractor)
class ContractorAdmin(admin.ModelAdmin):
    list_display = ['id', 'Name', 'Age' ,'payment']

@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'Name', 'Age' , 'Salary','role']

#'id', 'Name', 'Age' , 'Salary',
