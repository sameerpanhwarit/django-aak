from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Label(models.Model):
    name = models.CharField(max_length=100)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('name','owner')

    def __str__(self):
        return self.name
    

class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    labels = models.ManyToManyField(Label,blank=True)

    def __str__(self):
        return self.title