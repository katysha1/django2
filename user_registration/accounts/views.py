from http.client import HTTPResponse

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm


# Create your views here.
# def index(request):
#     return HTTPResponse("<h1>Добро пожаловать!</h1>")
    # return HTTPResponse("Добро пожаловать на главную страницу!")
    # return render(request, 'home.html')
#

def index(request):
     return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

