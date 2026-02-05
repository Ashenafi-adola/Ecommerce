from django.shortcuts import render, redirect
from .forms import CollectionForm, ProductForm
from . models import *


def home(request):
    q = request.GET.get('search') if request.GET.get('search') != None else ''
    products = Product.objects.filter(name__icontains=q).order_by('-pre_date')

    context = {
        'products':products,
    }
    return render(request, 'core/home.html', context)

def addProduct(request, id):
    collection = Collection.objects.get(id=id)
    page = 'pro'
    form = ProductForm()
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        print(request.POST.get('check'))
        if form.is_valid():
            product = form.save(commit=False)
            product.collection = collection
            product.save()
            return redirect('home')
    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'core/add_item.html', context)

def phoneDetails(request, id):
    phone = Product.objects.get(id=id)
    
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

def collection(request, id):
    collection = Collection.objects.get(id = id)
    products = Product.objects.filter(collection=collection)

    context = {
        'products':products,
        'collection':collection
    }
    return render(request, 'core/collection.html', context)

def product_details(request, id):
    product = Product.objects.get(id=id)
    
    context = {

    }
    return render(request, 'core/product_details.html', context)