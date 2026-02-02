from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import  login, authenticate, logout


def register(request):
    pass

def signin(request):
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('home')

    context = {

    }
    return render(request, 'accounts\login.html', context)

def register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
    
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)