from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name="home"),
    path('delete/<int:id>/', delete_task, name="delete_task"),
    path('update/<int:id>/', update_task, name="update_task"),
    path('complete/<int:id>/', complete_task, name="complete_task"),
]