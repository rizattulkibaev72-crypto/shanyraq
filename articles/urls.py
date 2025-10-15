from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    # статьи
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),

    # категории
    path('categories/', views.categories_list, name='categories_list'),
    path('categories/<slug:slug>/', views.category_detail, name='category_detail'),
    path('about/', views.about_view, name='about'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

]
    


