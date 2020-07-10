from django.shortcuts import render
from teachers.models import Teacher

def home(request):
    return render(request, 'assigner/assigner_home.html')

def manual(request):
    if request.method == 'POST':
        number = int(request.POST['number'])
        num_list = [x for x in range(1, number+1)]
        print(num_list)
        teachers = Teacher.objects.all()
        subjects = Teacher.objects.values('subject').order_by('subject')
        return render(request, 'assigner/manual.html', {'teachers': teachers, 'num_list':num_list, 'subjects': subjects})
    return render(request, 'assigner/manual.html')