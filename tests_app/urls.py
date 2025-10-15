from django.urls import path
from . import views

urlpatterns = [
    path('', views.tests_list, name='tests_list'),
    path('<slug:slug>/', views.test_detail, name='test_detail'),
    path('<slug:slug>/start/', views.test_start, name='test_start'),
]