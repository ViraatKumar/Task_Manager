from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.name

class Task(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    task_type = models.CharField(max_length=50, choices=(('personal', 'Personal'), ('work', 'Work')))
    completed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=(('pending', 'Pending'), ('completed', 'Completed')))
    users = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.name
