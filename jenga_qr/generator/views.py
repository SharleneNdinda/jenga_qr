from django.shortcuts import render


def index(request):
    context = {}
    return render(request, 'generator/index.html', context)

def generate(request):
    context = {}
    return render(request, 'generator/generate.html', context)
