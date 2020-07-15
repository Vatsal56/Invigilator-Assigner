from django.shortcuts import render, get_object_or_404, redirect
from teachers.models import Teacher
from .models import AssignedList
import datetime

def home(request):
    return render(request, 'assigner/assigner_home.html')

def manual(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        global num_list
        num_list = [x for x in range(1, number+1)]
        teachers = Teacher.objects.all()
        subjects = Teacher.objects.values('subject').order_by('subject')
        return render(request, 'assigner/manual.html', {'teachers': teachers, 'num_list':num_list, 'subjects': subjects})
    return render(request, 'assigner/manual.html')

def assigned(request):
    if request.method == 'POST':
        sub_teacher = []
        for num in num_list:
            sub_teacher.append([request.POST['subject' + str(num)], request.POST['teacher' + str(num)]])
        now = datetime.datetime.now()
        assigned_list = AssignedList()
        assigned_list.name = now.strftime("%Y-%m-%d")
        assigned_list.assigned = sub_teacher
        assigned_list.save()
        return redirect('/assigner/' + str(assigned_list.id))
    return render(request, 'assigner/manual.html')

def list_detail(request, list_id):
    assigned_list = get_object_or_404(AssignedList, pk=list_id)
    return render(request, 'assigner/list_detail.html', {'assigned_list':assigned_list})