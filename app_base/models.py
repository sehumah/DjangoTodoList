from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # establishes a 1 to many relationship
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created_time_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    # set the default ordering
    class Meta:
        ordering = ['complete']
