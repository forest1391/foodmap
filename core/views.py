from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyze(request):
    return render(request, 'analyze.html')

def coming(request):
    return render(request, 'coming.html')

def contact(request):
    return render(request, 'contact.html')

def single(request):
    return render(request, 'single.html')

def login(request):
    return render(request, 'login.html')

def community(request):
    return render(request, 'community.html')