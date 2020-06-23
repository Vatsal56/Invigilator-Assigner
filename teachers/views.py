from django.shortcuts import render

def home(request):
    return render(request, 'teachers/teachers_home.html')
