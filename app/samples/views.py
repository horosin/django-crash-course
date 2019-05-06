from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View
from django.views.generic import TemplateView

from django.contrib.auth.models import User
from .models import Sample, SampleType


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


def create(request):
    if request.method == "POST":
        try:
            name = request.POST['name']
            desc = request.POST['description']
            sample = Sample.objects.create(
                name=name, description=desc,
                created_by=User.objects.first(),
                type=SampleType.objects.first()    
            )
            sample.save()
            return redirect('index')
        except (KeyError):
            return render(request, 'samples/create.html',
                          {'error': 'Please fill all of the fields'})

    return render(request, 'samples/create.html', {})


class SampleAltCreateView(View):
    template_name = 'samples/create.html'
    redirect_to = 'index'

    def post(self, request):
        try:
            name = request.POST['name']
            desc = request.POST['description']
            sample = Sample.objects.create(
                name=name, description=desc,
                created_by=User.objects.first(),
                type=SampleType.objects.first()    
            )
            sample.save()
            return redirect(self.redirect_to)
        except (KeyError):
            return render(request, self.template_name,
                            {'error': 'Please fill all of the fields'})

    def get(self, request):
        return render(request, self.template_name, {})


class AboutView(TemplateView):
    template_name='samples/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context
