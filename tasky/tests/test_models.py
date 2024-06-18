#from hypothesis.extra.django import TestCase
import pytest
#from hypothesis import strategies as st, given
from tasky.models import *
from mixer.backend.django import mixer
pytestmark = pytest.mark.django_db


class TestTaskManagerModel:
    
    # Test if task with status can be created 
    def test_task_can_be_created(self):
        task1 = mixer.blend(TaskManager, title="Bug Fix", description="Fix bug for payment solution")
        task_result = TaskManager.objects.last()  # getting the last task
        assert task_result.title == "Bug Fix"
        assert task_result.description == "Fix bug for payment solution"

    def test_task_str_return(self):
        task1 = mixer.blend(TaskManager, title="Bug Fix")
        task_result = TaskManager.objects.last()  # getting the last task
        assert str(task_result) == "Bug Fix"
