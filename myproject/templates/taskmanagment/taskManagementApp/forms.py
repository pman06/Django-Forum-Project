from .models import TaskDb
from django import forms


class TaskForm(forms.ModelForm):
    class Meta:
        model = TaskDb
        fields = ['task', 'priority']
