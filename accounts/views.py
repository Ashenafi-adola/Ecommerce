from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login, authenticate, logout


def register(request):
    pass

def signin(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)

    context = {
        'form': form,
    }
    return render(request, 'accounts\login.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            
            return 