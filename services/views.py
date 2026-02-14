from django.shortcuts import render
from .models import ServicePackage

def services_list(request):
    packages = ServicePackage.objects.all()
    return render(request, 'services/services_list.html', {'packages': packages})
