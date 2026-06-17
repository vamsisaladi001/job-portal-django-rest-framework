from django.db import models

# Create your models here.
from django.db import models

class User(models.Model):

    ROLE_CHOICES = (
        ('Recruiter', 'Recruiter'),
        ('Candidate', 'Candidate'),
    )

    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    def __str__(self):
        return self.username