from django.contrib import admin
from . models import *
# Register your models here.
@admin.register((Employee))
class EmployeeModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','password','company','areacode','contact','subject']