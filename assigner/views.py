from django.shortcuts import render

def home(request):
    return render(request, 'assigner/assigner_home.html')