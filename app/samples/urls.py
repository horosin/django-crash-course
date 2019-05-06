from django.urls import path
from . import views

urlpatterns = [
    path('other/', views.other_page, name='other'),
    path('<int:sample_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('', views.index, name='index'),
]
