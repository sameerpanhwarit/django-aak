from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Label, Task
from .serializers import TaskSerializer, LabelSerializer
from .permissions import isOwner

# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class =  TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)


class LabelViewSet(viewsets.ModelViewSet):
    serializer_class =  LabelSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Label.objects.filter(owner=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(owner = self.request.user)

