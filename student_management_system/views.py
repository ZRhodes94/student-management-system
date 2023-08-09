from django.shortcuts import render
from .models import Teacher, Student, Parent, Assignment, Grade, Behavior, Course
from .forms import AssignmentForm


# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    courses = Course.objects.filter(teacher = 1).order_by('time')
    context = {"teacher": teacher, "courses": courses}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def contact_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    context = {"teacher": teacher}
    template = loader.get_template('contact.html')
    return HttpResponse(template.render(context, request))

def class_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    context = {"teacher": teacher}
    template = loader.get_template('class-info.html')
    return HttpResponse(template.render(context, request))

def assignments_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    courses = Course.objects.filter(teacher = 1).order_by('time')
    assignments = Assignment.objects.all()
    context = {"teacher": teacher, "courses": courses, "assignments":assignments}
    template = loader.get_template('assignments.html')

    if request.method == 'POST':
        form = AssignmentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))

def behavior_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    context = {"teacher": teacher}
    template = loader.get_template('behavior.html')
    return HttpResponse(template.render(context, request))