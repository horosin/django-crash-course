from django.urls import path

from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('other/', views.other_page, name='other'),
    path('<int:sample_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('create_alt', views.SampleAltCreateView.as_view(), name='create_alt'),
    path('about/', TemplateView.as_view(template_name="samples/about.html"), name='about'),
    path('', views.index, name='index'),
]
