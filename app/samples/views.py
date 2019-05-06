from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View, generic

from django.contrib.auth.models import User
from .models import Sample, SampleType


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)


class SampleListView(generic.ListView):
    model = Sample


class SampleDetailView(generic.DetailView):
    model=Sample


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


class AboutView(generic.TemplateView):
    template_name='samples/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context
