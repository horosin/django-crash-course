from django.urls import path
from . import views

urlpatterns = [
    path('other', views.other_page, name='other'),
    path('', views.index, name='index'),
]
