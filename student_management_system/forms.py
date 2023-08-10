from django import forms
from .models import Assignment, Teacher, Student, Behavior, Course, Grade, Parent

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['name', 'course', 'dueDate', 'pointsPossible', 'description']

class BehaviorForm(forms.ModelForm):
    class Meta:
        model = Behavior
        fields = ['description', 'interventions', 'student', 'date']