from django.urls import path
from . import views

urlpatterns = [
    path('home', views.homeTest),
    path('', views.taskList, name='task-list'),
    path('yourname/<str:name>', views.yourName, name='your-name'),
]