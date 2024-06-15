from .models import *
from rest_framework import serializers, exceptions

class TaskManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskManager
        fields = '__all__'
        