from django.shortcuts import render
from django.http import HttpResponse


from .models import Sample


def index(request):
    samples = Sample.objects.all()
    return render(request, 'samples/index.html', {"samples": samples})


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)
