import pytest
from tasky.models import *
from mixer.backend.django import mixer
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.reverse import reverse
pytestmark = pytest.mark.django_db


class TestTaskAPI(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Test if task with overdue status can be created and retrieve
    def test_tasks_overdue(self):
        task1 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='Overdue')
        task2 = mixer.blend(TaskManager, title="Technical upgrade", description="Perform technical upgrade payment solution", status='Completed')
        task3 = mixer.blend(TaskManager, title="Improve Onboarding", description="Improving user onboarding process", status='In Progress')
        task4 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='Overdue')

        allTasks = TaskManager.objects.filter(status='Overdue')
        self.assertEqual(len(allTasks), 2)

    
    # Test if task with completed status can be created and retrieve
    def test_tasks_completed(self):
        task1 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='Overdue')
        task2 = mixer.blend(TaskManager, title="Technical upgrade", description="Perform technical upgrade payment solution", status='Completed')
        task3 = mixer.blend(TaskManager, title="Improve Onboarding", description="Improving user onboarding process", status='In Progress')
        task4 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='Completed')

        allTasks = TaskManager.objects.filter(status='Completed')
        self.assertEqual(len(allTasks), 2)

    # Test if task with In Progress status can be created and retrieve
    def test_tasks_in_progress(self):
        task1 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='Overdue')
        task2 = mixer.blend(TaskManager, title="Technical upgrade", description="Perform technical upgrade payment solution", status='Completed')
        task3 = mixer.blend(TaskManager, title="Improve Onboarding", description="Improving user onboarding process", status='In Progress')
        task4 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution", status='In Progress')

        allTasks = TaskManager.objects.filter(status='In Progress')
        self.assertEqual(len(allTasks), 2)