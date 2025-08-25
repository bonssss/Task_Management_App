from django.urls import path
from .views import UserCreateView, TaskListCreateView, TaskDetailView, MarkCompleteView, MarkIncompleteView

urlpatterns = [
    path('users/', UserCreateView.as_view(), name='user-create'),
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailView.as_view(), name='task-detail'),
    path('tasks/<int:pk>/complete/', MarkCompleteView.as_view(), name='task-complete'),
    path('tasks/<int:pk>/incomplete/', MarkIncompleteView.as_view(), name='task-incomplete'),
]
