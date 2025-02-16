
from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name="index"),
    path('/<str:item>/', views.course, name="Course"),
    path('/<int:num1>/<int:num2>', views.multiply, name="Course"),
]
