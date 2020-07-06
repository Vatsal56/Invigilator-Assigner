from django.http import HttpResponse
from django.shortcuts import render
from openpyxl import load_workbook

def homepage(request):
    wb = load_workbook(filename = 'invigilatorassignment/excel/trial.xlsx')
    ws = wb.active
    timetable = []
    for row in ws.values:
        timetable.append(list(row))
    return render(request, 'home.html', {'timetable':timetable})
    