from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiCommands, name="api-cmds"),
    path('task-list/', views.taskList, name="task-list")
]