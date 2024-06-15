from django.shortcuts import render,render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
from django.contrib import messages
# from django.views.generic import DetailView, ListView
# from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse,reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from .forms import *


def index(request):
    return render(request, 'index.html')

class TaskCreate(LoginRequiredMixin, CreateView, SuccessMessageMixin):
	model = TaskManager
	template_name = 'task/create.html'
	form_class = TaskForm
  
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TaskCreate, self).form_valid(form)

	def get_success_url(self):
		messages.success(self.request, 'Your Paper has been Submitted Successfully!! ')
		return '/' # or whatever url you want to redirect to

class TaskDetail(DetailView):
    model = TaskManager
    template_name = 'task/detail.html'


class TaskUpdate(LoginRequiredMixin, UpdateView):
	model = TaskManager
	template_name = 'task/create.html'
	form_class = TaskForm
  
	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(TaskUpdate, self).form_valid(form)

	def get_success_url(self):
		messages.success(self.request, 'you have successfully updated')
		return '/' # or whatever url you want to redirect to


class TaskDelete(DeleteView):
    model = TaskManager
    template_name = 'task/task_confirm_delete.html'
    
    def get_success_url(self):
        messages.success(self.request, 'you have successfully deleted task')
        return '/' # or whatever url you want to redirect to


class TaskManagerViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for task.
    """
    queryset = TaskManager.objects.all()
    serializer_class = TaskManagerSerializer
    permission_classes = [IsAuthenticated]
    
    def list(self, request):
        try:
            # Check to see if task exists for a particular user
            # and display it/them
            allTasks = TaskManager.objects.filter(user=request.user) 
            if allTasks.exists():
                serializer = self.get_serializer(allTasks, many=True)
                publish('task Listing', serializer.data) # create a socket stream
                return Response(serializer.data, status=status.HTTP_200_OK) # return task oject response
            else:
                return Response(
                    {"message": ["User has no task yet"]},
                    status=status.HTTP_400_BAD_REQUEST,
                ) # return error response

        except Exception as e:
            return Response({"message": f"{e}"}, status=status.HTTP_400_BAD_REQUEST) # return error response
