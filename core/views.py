from django.shortcuts import render


def home(request):

    context = {

    }
    return render(request, 'core/home.html', context)

def addItems(request):

    context = {
        
    }
    return render(request, 'core/add_item.html', context)