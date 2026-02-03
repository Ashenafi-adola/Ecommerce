from django.shortcuts import render, redirect
from .forms import CollectionForm, ProductForm
from . models import *


def home(request):

    context = {

    }
    return render(request, 'core/home.html', context)

def addProduct(request):
    page = 'pro'
    form = ProductForm()
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'core/add_item.html', context)

def addCollection(request):
    page = 'col'
    form = CollectionForm()
    if request.method == 'POST':
        form = CollectionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'core/add_item.html', context)

def collections(request):
    collections = Collection.objects.all()

    context = {
        'collections':collections,
    }
    return render(request, 'core/collections.html', context)