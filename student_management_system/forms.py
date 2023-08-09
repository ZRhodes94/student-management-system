from django import forms
from .models import Assignment, Teacher, Student, Behavior, Course, Grade, Parent

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        field = ['name', 'description', 'pointsPossible', 'course', 'dueDate']