from rest_framework import serializers
from.models import Task, Label

class LabelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Label
        fields = '__all__'
        read_only_fields = ['owner']


class TaskSerializer(serializers.ModelSerializer):
    labels = LabelSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['owner']
