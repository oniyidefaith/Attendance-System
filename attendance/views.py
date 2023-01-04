from django.shortcuts import render, redirect
from .models import *
from .forms import UpdateStudentForm, Attendance


# Create your views here.
def home(request):
    return render(request, "home.html")


def student_data(request):
    stud_data = StudentDataInfo.objects.all()
    context = {'datas': stud_data}
    return render(request, "student_data.html", context)


def add_student_info(request):
    if request.method == 'POST':
        matric_no = request.POST['MatricNo']
        name = request.POST['Student_name']
        gender = request.POST['Gender']
        email = request.POST['Email']
        level = request.POST['Level']
        department = request.POST['Department']
        semester = request.POST['Semester']
        session = request.POST['Session']

        stundent = StudentDataInfo.objects.create(matric_no=matric_no, name=name, gender=gender, email=email,
                                                  level=level, department=department, semester=semester,
                                                  session=session)
        stundent.save()
        print('saved!')
        return redirect('student-data')

    context = {}
    return render(request, "student_form.html", context)


def update_student_info(request, pk):
    student = StudentDataInfo.objects.get(id=pk)
    form = UpdateStudentForm(instance=student)
    if request.method == 'POST':
        form = UpdateStudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student-data')

    context = {'form': form}
    return render(request, "update-form.html", context)


def delete_student_info(request, pk):
    student = StudentDataInfo.objects.get(id=pk)
    student.delete()
    return redirect('student-data')


# Here Comes The Logic
def successful(request):
    return render(request, 'succesful.html')


def do_attendance(request):
    if request.method == 'POST':
        form = Attendance(request.POST)
        if form.is_valid():
            form.save()
            return redirect('successful')
    else:
        form = Attendance()
    context = {'form': form}
    return render(request, 'attendance.html', context)


def attendance_table(request):
    attendance = AttendanceTable.objects.all()
    context = {'attendance': attendance}
    return render(request, 'attendance_table.html', context)


def overall_report(request):
    return render(request, 'overall_report.html')


def create_student_view(request):
    if request.method == 'POST':
        matric_number = request.POST['matric_number']
        name = request.POST['name']


def get_student_view(request):
    students = CreateStudent.objects.all()
    context = {'students': students}
    return render(request, context)
