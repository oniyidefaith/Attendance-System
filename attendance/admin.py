from django.contrib import admin
from .models import StudentDataInfo, AttendanceTable

# Register your models here.
admin.site.register(StudentDataInfo)
admin.site.register(AttendanceTable)