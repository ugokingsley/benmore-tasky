from django.db import models
from core.models import *

STATUS = (
	('In Progress', 'In Progress'),
	('Completed', 'Completed'),
	('Overdue', 'Overdue'),
) 

PRIORITY = (
	('Low', 'Low'),
	('Medium', 'Medium'),
	('High', 'High'),
) 

class TaskManager(models.Model):
    title = models.CharField(max_length=240, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=100, choices=STATUS, blank=True, null=True)
    priority = models.CharField(max_length=100, choices=PRIORITY, blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=240, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)   
    
    # a toString method that returns the book title
    def __str__(self):
        return str(self.title)

    # default ordering by primary key (id) in descending order    
    class Meta:
        ordering = ["-pk"]