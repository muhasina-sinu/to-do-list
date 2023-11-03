from django.urls import path
from .views import ListView, CreateView, UpdateView, DeleteView

urlpatterns = [
    path('list/', ListView.as_view(), name='task_list'),
    path('create/', CreateView.as_view(), name='task_create'),
    path('update/<int:pk>/', UpdateView.as_view(), name='task_update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='task_delete'),
]
