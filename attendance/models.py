from django.db import models

# Create your models here.


class StudentDataInfo(models.Model):
    matric_no   = models.CharField(max_length=100, blank=True, null=True)
    name        = models.CharField(max_length=400, blank=True, null=True)
    gender      = models.CharField(max_length=100, blank=True, null=True)
    email       = models.EmailField(max_length=254)
    session     = models.CharField(max_length=100, blank=True, null=True)
    level       = models.CharField(max_length=100, blank=True, null=True)
    department  = models.CharField(max_length=250, blank=True, null=True)
    semester    = models.CharField(max_length=100, blank=True, null=True)


    def __str__(self):
        return f"{self.matric_no}"



class AttendanceTable(models.Model):
    matricNumber = models.ForeignKey(StudentDataInfo, on_delete=models.CASCADE, blank=True, null=False)
    present = models.BooleanField(default=False)


   






    def what_to_return(self):
        if self.present:
            return 'Yes'
        else:
            return 'No'

    def __str__(self):
        if self.present:
            return 'present'
        else:
            return 'absent'