from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.create_task, name='create_task'),
    # Take task id as query input
    path('tasks/<int:task_id>/assign/', views.assign_task, name='assign_task'),
    # Take User id as query input here as well
    path('users/<int:user_id>/tasks/', views.get_tasks_for_user, name='get_tasks_for_user'),
    path('users/', views.create_user, name='create_user'), 
    path('',views.default_page,name="default_page")
]
