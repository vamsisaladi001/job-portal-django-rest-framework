from django.db import models

# Create your models here.
from django.db import models
from users.models import User
from job.models import Job

class Application(models.Model):

    STATUS_CHOICES = (
        ('Applied', 'Applied'),
        ('Shortlisted', 'Shortlisted'),
        ('Rejected', 'Rejected'),
        ('Selected', 'Selected'),
    )

    candidate = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Candidate'}
    )

    job = models.ForeignKey(Job, on_delete=models.CASCADE)

    resume = models.FileField(upload_to='resumes/')

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Applied'
    )

    def __str__(self):
        return f"{self.candidate.username} - {self.job.title}"