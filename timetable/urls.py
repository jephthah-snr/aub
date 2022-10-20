from . import views
from django.urls import path
app_name = 'timetable'

urlpatterns = [
    path('<str:day>/', views.index, name='index'),
    path('create_task/', views.create_task, name='create_task'),
]
