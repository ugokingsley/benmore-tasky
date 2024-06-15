from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.forms import ModelForm, Textarea

from .models import *


class TaskForm(forms.ModelForm):
	class Meta:
		model = TaskManager
		fields = '__all__'
