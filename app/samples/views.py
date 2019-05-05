from django.shortcuts import render, get_object_or_404
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


def detail(request, sample_id):
    sample = get_object_or_404(Sample, pk=sample_id)
    return render(request, 'samples/detail.html', {'sample': sample})
