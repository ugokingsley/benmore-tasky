from django.shortcuts import render,render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from .models import *
from .serializers import *
from .forms import *

# returns the tasks HTML template
def index(request):
    all_users = User.objects.all() 
    context = {
		'all_users': all_users,
	}
    return render(request, 'task/index.html', context=context)

class TaskManagerViewSet(ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for task.
    """
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer
    permission_classes = [IsAuthenticated]

    @action(methods=["GET"], detail=False)
    def tasks_overdue(self, request):
        try:
            # Check to see if task exists for a particular user
            # and display it/them
            allTasks = TaskManager.objects.filter(status='Overdue')  
            if allTasks.exists():
                serializer = self.get_serializer(allTasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
            else:
                return Response(
                    {"message": ["User has no task yet"]},
                    status=status.HTTP_400_BAD_REQUEST,
                ) # return error response

        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST) # return error response

    @action(methods=["GET"], detail=False)
    def tasks_completed(self, request):
        try:
            # Check to see if task exists for a particular user
            # and display it/them
            allTasks = TaskManager.objects.filter(status='Completed')  
            if allTasks.exists():
                serializer = self.get_serializer(allTasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
            else:
                return Response(
                    {"message": ["User has no task yet"]},
                    status=status.HTTP_400_BAD_REQUEST,
                ) # return error response

        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST) # return error response


    @action(methods=["GET"], detail=False)
    def tasks_in_progress(self, request):
        try:
            # Check to see if task exists for a particular user
            # and display it/them
            allTasks = TaskManager.objects.filter(status='In Progress')  
            if allTasks.exists():
                serializer = self.get_serializer(allTasks, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
            else:
                return Response(
                    {"message": ["User has no task yet"]},
                    status=status.HTTP_400_BAD_REQUEST,
                ) # return error response

        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST) # return error response

    def create(self, request):
        serializer = TaskManagerSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True) # check all fields is valid before attempting to save
        # serializer.save(assigned_to=self.request.user)
        serializer.save()
        return Response({
            "status": 201,
            "message": ["Task Created Successfully"]},
            status=status.HTTP_201_CREATED,
            ) # return task oject response

    def retrieve_task(self, request, *args, **kwargs):
        # retrieve/read task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            #any additional logic
            serializer = self.get_serializer(instance)
            return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response

    def update_task(self, request, *args, **kwargs):
        # update task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            serializer = self.get_serializer(instance)
            super().update(request, *args, **kwargs)
            return Response({'message':'Task Updated Successfully'}, status=status.HTTP_200_OK) # return task oject response
    
    def destroy_task(self, request, *args, **kwargs):
        # Delete task by id created by a particular user 
        # check if task exists, throw an error is it doesn't
        try:
            instance = self.get_object()
        except Exception as e:
            return Response({'message':str(e)}, status=status.HTTP_204_NO_CONTENT,) # return error response
        else:
            serializer = self.get_serializer(instance)
            instance.delete()
            publish('Task Deleted Successfully', serializer.data) # create a socket stream
            return Response({'message':'Task Deleted'}, status=status.HTTP_204_NO_CONTENT) # return task oject response