from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task
from django.utils.timezone import now

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data.get('email'),
            password=validated_data['password']
        )
        return user


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Task
        fields = '__all__'

    def validate_due_date(self, value):
        if value < now():
            raise serializers.ValidationError("Due date must be in the future.")
        return value
