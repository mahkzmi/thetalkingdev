# views.py
from django.shortcuts import render
from .models import Project

def project_list(request):
    projects = Project.objects.all()  # اینجا باید همه پروژه‌ها رو بگیرید
    return render(request, 'projects/project_list.html', {'projects': projects})