from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def login_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home_view(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())

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