from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('student_list/', views.student_list, name='list'),
    path('student_create/', views.student_create, name="create"),
    path('student_update/<int:pk>/', views.student_update, name="update"), 
    path('student_delete/<int:pk>/', views.student_delete, name="delete"),
]