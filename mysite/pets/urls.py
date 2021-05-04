from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name = 'pets'
urlpatterns = [
    path('', views.PetList.as_view(), name='all'),
    path('main/create/', views.PetCreate.as_view(), name='pet_create'),
    path('main/<int:pk>/update/', views.PetUpdate.as_view(), name='pet_update'),
    path('main/<int:pk>/delete/', views.PetDelete.as_view(), name='pet_delete'),
    path('lookup/', views.TypeList.as_view(), name='type_list'),
    path('lookup/create/', views.TypeCreate.as_view(), name='type_create'),
    path('lookup/<int:pk>/update/', views.TypeUpdate.as_view(), name='type_update'),
    path('lookup/<int:pk>/delete/', views.TypeDelete.as_view(), name='type_delete'),
]
