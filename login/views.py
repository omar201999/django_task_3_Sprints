from django.shortcuts import render
from .forms import LoginForm
# Create your views here.


def login(request):
    if request.method == 'POST':
        dataForm = LoginForm(request.POST)
        if dataForm.is_valid():
            dataForm.save()
    return render(request, 'login_form.html', {'login_form': LoginForm})
