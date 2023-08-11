from django.shortcuts import render
from django.urls import reverse
from urllib.parse import urlsplit
from .models import Teacher, Student, Parent, Assignment, Grade, Behavior, Course
from .forms import AssignmentForm, BehaviorForm, GradeForm



# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader


def login_view(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())

def home_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    courses = Course.objects.filter(teacher = 1).order_by('time')
    assignments = Assignment.objects.all()
    context = {"teacher": teacher, "courses": courses, "assignments": assignments}
    template = loader.get_template('home.html')
    return HttpResponse(template.render(context, request))

def class_view(request, id):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    students = Student.objects.filter(courses=id)
    assignments = Assignment.objects.filter(course=id)
    grades = Grade.objects.filter(assignment__course=id).order_by('student')
    context = {"teacher": teacher, "grades": grades, "students": students, "assignments": assignments}
    context["course"] = Course.objects.get(id = id)
    template = loader.get_template('class-info.html')
    
    if request.method == 'POST':
        form = GradeForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))

def assignments_view(request):
    teacher = Teacher.objects.get(name='Zachary Rhodes')
    courses = Course.objects.filter(teacher = 1).order_by('time')
    assignments = Assignment.objects.all()
    assignment_form = AssignmentForm()
    context = {"teacher": teacher, "courses": courses, "assignments":assignments, "assignment_form": assignment_form}
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
    behaviors = Behavior.objects.all()
    students = Student.objects.all()
    context = {"teacher": teacher, "behaviors": behaviors, "students": students}
    template = loader.get_template('behavior.html')
    
    if request.method == 'POST':
        form = BehaviorForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))
    
def delete_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    assignment.delete()
    return HttpResponseRedirect(reverse('assignments_view'))

def delete_behavior(request, id):
    behavior = Behavior.objects.get(id=id)
    behavior.delete()
    return HttpResponseRedirect(reverse('behavior_view'))

def delete_grade(request, course_id, grade_id):
    grade = Grade.objects.get(id=grade_id)
    grade.delete()
    
    return HttpResponseRedirect(reverse('class_view', kwargs={'id': course_id}))

def edit_assignment(request, id):
    assignment = Assignment.objects.get(id=id)
    context = {"assignment": assignment}
    template = loader.get_template('assignments_edit.html')

    if request.method == 'POST':
        form = AssignmentForm(request.POST or None)
        if form.is_valid():
            form.save()
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse(template.render(context, request))

def edit_behavior(request, id):
    behavior = Behavior.objects.get(id=id)
    context = {"behavior": behavior}
    template = loader.get_template('behavior_edit.html')

    return HttpResponse(template.render(context, request))

def edit_grade(request, course_id, grade_id):
    grade = Grade.objects.get(id=grade_id)
    context = {"grade": grade}
    template = loader.get_template('class-info_edit.html')
    
    return HttpResponse(template.render(context, request))

def updaterecord_assignment(request, id):
  name = request.POST['name']
  course = request.POST['course']
  dueDate = request.POST['dueDate']
  pointsPossible = request.POST['pointsPossible']
  description = request.POST['description']
  assignment = Assignment.objects.get(id=id)
  assignment.name = name
  assignment.course = course
  assignment.dueDate = dueDate
  assignment.pointsPossible = pointsPossible
  assignment.description = description
  assignment.save()
  return HttpResponseRedirect(reverse('assignments_view'))