from django import forms
from . models import Task  # Import the Task model from models.py

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task  # Associate the form with the Task model
        fields =['title','completed']  # Define the fields you want in the form
