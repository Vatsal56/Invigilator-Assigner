from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db.models import Q
from .models import Teacher

def home(request):
    teachers = Teacher.objects.order_by('name')
    return render(request, 'teachers/teachers_home.html', {'teachers':teachers})

def detail(request):
    return render(request, 'teachers/detail.html')

def search(request):
    if request.method == 'POST':
        search = request.POST['search']
        if search:
            match = Teacher.objects.filter(Q(name__icontains=search) | Q(subject__icontains=search))
            if match:
                return render(request, 'teachers/search.html', {'match':match})
            else:
                return render(request, 'teachers/search.html', {'error':'No Results Found'})
        else:
            return HttpResponseRedirect('teachers/teachers_home.html')
    return render(request, 'teachers/teachers_home.html')