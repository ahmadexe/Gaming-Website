from django.http import HttpResponse
from django.shortcuts import render
import webbrowser


def index(request):
    return render(request, 'index.html')


def available(request):
    return render(request, 'available.html')


def future(request):
    return render(request, 'future.html')


def search(request):
    text = request.GET.get('text', 'default')
    return HttpResponse(webbrowser.open(f"https://www.google.com/search?q={text}"))    
