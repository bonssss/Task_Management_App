from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.views import APIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

# User CRUD
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


# Task CRUD
class TaskListCreateView(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    ordering_fields = ['due_date', 'priority']

    def get_queryset(self):
        queryset = Task.objects.filter(user=self.request.user)

        # Get query params and strip whitespace
        status = self.request.query_params.get('status')
        if status:
            queryset = queryset.filter(status__iexact=status.strip())

        priority = self.request.query_params.get('priority')
        if priority:
            queryset = queryset.filter(priority__iexact=priority.strip())

        return queryset

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TaskDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def update(self, request, *args, **kwargs):
        task = self.get_object()
        if task.status == 'completed' and request.data.get('status') != 'pending':
            return Response({"error": "Cannot edit a completed task unless reverting to incomplete."}, status=400)
        return super().update(request, *args, **kwargs)


# # Mark complete/incomplete
# class MarkCompleteView(APIView):
#     def post(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk, user=request.user)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found"}, status=404)
#         task.mark_complete()
#         return Response({"status": "Task marked as complete"})


# class MarkIncompleteView(APIView):
#     def post(self, request, pk):
#         try:
#             task = Task.objects.get(pk=pk, user=request.user)
#         except Task.DoesNotExist:
#             return Response({"error": "Task not found"}, status=404)
#         task.mark_incomplete()
#         return Response({"status": "Task marked as incomplete"})


class MarkCompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        if task.status == 'completed':
            return Response({"error": "Task is already completed"}, status=400)
        task.mark_complete()
        return Response({"status": "Task marked as complete",
                         "completed_at": task.completed_at})


class MarkIncompleteView(APIView):
    permission_classes = [IsAuthenticated]

    def patch(self, request, pk):
        try:
            task = Task.objects.get(pk=pk, user=request.user)
        except Task.DoesNotExist:
            return Response({"error": "Task not found"}, status=404)
        task.mark_incomplete()
        return Response({"status": "Task marked as incomplete"})
