from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import View, generic
from django.urls import reverse_lazy

from django.contrib.auth.models import User
from .models import Sample, SampleType


def other_page(request):
    context = {
        'test': 'passing a value to the template'
    }
    return render(request, 'samples/other.html', context)


class SampleCreateView(generic.CreateView):
    model = Sample
    fields = '__all__'
    success_url = reverse_lazy('index')


class SampleUpdateView(generic.UpdateView):
    model = Sample
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('detail', args=[self.kwargs['pk']])


class SampleListView(generic.ListView):
    model = Sample


class SampleDetailView(generic.DetailView):
    model = Sample


class AboutView(generic.TemplateView):
    template_name = 'samples/about.html'

    def get_context_data(self):
        context = {'dynamic_val': 'this info changes'}
        return context
