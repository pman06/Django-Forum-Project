from django.db import models
from django.utils import timezone

# Create your models here.
class TaskDb(models.Model):
    task = models.CharField(max_length = 30)
    priority = models.CharField(max_length = 30)
    completed = models.BooleanField(default=False)
    time_date = models.DateTimeField(default = timezone.now)

    def __str__(self):
        return "%s %s"%(self.task, self.completed)
