from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index)
    path('', views.dashboard, name='dashboard'),
    path('add/', views.add_task, name='add_task'),
    path('tasks/', views.view_tasks, name='view_tasks'),
    path('tasks/edit/<int:task_id>/', views.edit_task, name='edit_task'), 
    path('tasks/delete/<int:task_id>/', views.delete_task, name='delete_task'), 
]