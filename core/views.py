from django.shortcuts import render
from .forms import CollectionForm, ProductForm


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
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'core/add_item.html', context)