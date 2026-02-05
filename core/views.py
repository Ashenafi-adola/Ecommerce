from django.shortcuts import render, redirect
from .forms import CollectionForm, ProductForm, PhoneInfoForm
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
        if form.is_valid() and request.POST.get('check') == 'on':
            product = form.save(commit=False)
            product.collection = collection
            product.save()
            return redirect(f'/core/phone-info/{product.id}')
        elif form.is_valid():
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
    form = PhoneInfoForm()
    if request.method == 'POST':
        form = PhoneInfoForm(request.POST)
        if form.is_valid():
            pho = form.save(commit=False)
            pho.product = phone
            pho.save()
            return redirect('home')
    context = {
        'form':form,
    }
    return render(request, 'core/more_info.html', context)

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
    phoneinfo = None
    try:
        phoneinfo = PhoneInfo.objects.get(product=product)
        info = 'exist'
    except Exception:
        info = "not exist"

    if request.user not in product.views.all():
        product.views.add(request.user)
    if request.method == 'POST' and request.user not in product.likes.all():
        product.likes.add(request.user)
    elif request.method == 'POST' and request.user in product.likes.all():
        product.likes.remove(request.user)

    context = {
        'product':product,
        'phoneinfo': phoneinfo,
        'info': info,
    }
    return render(request, 'core/product_detail.html', context)

def editProductDetails(request, id):
    page = 'pro'
    product = Product.objects.get(id=id)
    form = ProductForm(instance=product)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid() and request.POST.get('check') == 'on':
            product = form.save(commit=False)
            product.save()
            return redirect(f'/core/edit-details1/{product.id}')
        elif form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect(f'/core/product-details/{id}/')


    context = {
        'form':form,
        'page':page,
    }
    return render(request, 'core/edit_details.html', context)

def editProductDetails1(request, id):
    product = Product.objects.get(id=id)
    info = PhoneInfo.objects.get(product=product)
    form = PhoneInfoForm(instance=info)
    if request.method == 'POST':
        form = PhoneInfoForm(request.POST, instance=info)
        if form.is_valid():
            moreinfo = form.save(commit=False)
            moreinfo.save()
            return redirect(f'/core/product-details/{id}/')
        
    context = {
        'form':form,
    }
    return render(request, 'core/edit_details.html', context)
