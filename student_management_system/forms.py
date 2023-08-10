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

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['pointsEarned', 'assignment', 'student']

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)