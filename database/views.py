from django.shortcuts import render, redirect
from .models import Staff

# Create your views here.

def home(request):
    staffs = Staff.objects.all()
    return render(request, 'individual_member.html', {'staffs': staffs})