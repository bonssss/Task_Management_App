from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Task(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    completed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
    
    def mark_complete(self):
        if self.status != 'completed':
            self.status = 'completed'
            self.completed_at = timezone.now()
            self.save()

    def mark_incomplete(self):
        if self.status == 'completed':
            self.status = 'pending'
            self.completed_at = None
            self.save()
    

    class Meta:
        ordering = ['-created_at']
