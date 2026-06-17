from django.db import models

# Create your models here.
from django.db import models
from users.models import User

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.IntegerField()
    description = models.TextField()

    recruiter = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Recruiter'}
    )

    def __str__(self):
        return self.title