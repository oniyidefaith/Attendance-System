from django.forms import ModelForm
from django import forms
from .models import StudentDataInfo, AttendanceTable

class UpdateStudentForm(ModelForm):
    class Meta:
        model = StudentDataInfo
        fields = '__all__'

class Attendance(ModelForm):

    class Meta:
        model = AttendanceTable
        fields = '__all__'

