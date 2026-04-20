from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('adminlogin/', views.adminlogin, name='adminlogin'),
    path('add_doctor/', views.add_doctor, name='add_doctor'),
    path('view_doctors/', views.view_doctors, name='view_doctors'),
    path('delete_doctor/<int:id>/', views.delete_doctor, name='delete_doctor'),
    path('add_patient/', views.add_patient, name='add_patient'),
    path('view_patients/', views.view_patients, name='view_patients'),
    path('logout/', views.logout, name='logout'),
]