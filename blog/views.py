from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context = {
        'message': 'ARQUIVO INDEX'
    }
    return render(request, 'index.html', context)

def post(request):
    context = {
        'message': 'ARQUIVO POST'
    }
    return render(request, 'post.html', context)

def about(request):
    context = {
        'message': 'ARQUIVO ABOUT'
    }
    return render(request, 'about.html', context)