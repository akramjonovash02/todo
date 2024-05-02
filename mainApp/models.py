from django.db import models
from django.contrib.auth.models import User

STATUS_CHOICES = (
    ('new', 'new'),
    ('in progress', 'in progress'),
    ('complited', 'complited')
)

class Task(models.Model):
    title = models.CharField(max_length=255)
    description= models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new')
    deadline = models.DateField(blank=True, null=True)
    created_at= models.DateField(auto_now_add=True)
    updated_at=models.DateField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username}: {self.title}"

