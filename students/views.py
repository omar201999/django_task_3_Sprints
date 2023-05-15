from django.shortcuts import render

from .models import Student

# Create your views here.


def students(request):
    context = {}
    context["dataset"] = Student.objects.all()
    return render(request, 'index.html', context)
