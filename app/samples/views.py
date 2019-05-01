from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)
