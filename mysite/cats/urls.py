from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/4.2/topics/http/urls/
app_name = 'cats'

urlpatterns = [
    path('', views.MainView.as_view(), name='all'),
    path('main/create/', views.CatsCreate.as_view(), name='cat_create'),
    path('main/<int:pk>/update/', views.CatsUpdate.as_view(), name='cat_update'),
    path('main/<int:pk>/delete/', views.CatsDelete.as_view(), name='cat_delete'),

    path('lookup/', views.BreedsView.as_view(), name='breed_list'),
    path('lookup/create/', views.BreedsCreate.as_view(), name='breed_create'),
    path('lookup/<int:pk>/update/', views.BreedsUpdate.as_view(), name='breed_update'),
    path('lookup/<int:pk>/delete/', views.BreedsDelete.as_view(), name='breed_delete'),
]