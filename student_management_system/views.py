from django.shortcuts import render
from .models import Teacher, Student, Parent, Assignment, Grade, Behavior, Course


# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home_view(request):
    teacher_name = Teacher.objects.filter(name='Zachary Rhodes').values()
    courses = Course.objects.filter(teacher = 'Zachary Rhodes').values()
    context = {"teacher_name": teacher_name, "courses": courses}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def contact_view(request):
    template = loader.get_template('contact.html')
    return HttpResponse(template.render())

def class_view(request):
    template = loader.get_template('class-info.html')
    return HttpResponse(template.render())

def assignments_view(request):
    template = loader.get_template('assignments.html')
    return HttpResponse(template.render())

def behavior_view(request):
    template = loader.get_template('behavior.html')
    return HttpResponse(template.render())