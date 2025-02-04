from django.urls import path
from .import views
  
urlpatterns = [
    path('', views.office_list, name='office_list'),
    path('create/', views.office_create, name='office_create'),
    path('office/<int:office_id>/', views.office_detail, name='office_detail'),
    path('office/<int:office_id>/delete/', views.office_delete, name='office_delete'),
]

    
