from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    done = models.BooleanField(default=False, blank=True)

    def __str__(self):
        return self.title