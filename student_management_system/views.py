from django.shortcuts import render
from .models import Teacher, Student, Parent, Assignment, Grade, Behavior, Course
from .forms import AssignmentForm, BehaviorForm, GradeForm, ContactForm



# Create your views here.
from django.http import HttpResponse
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

def contact_view(request):
    if request.method == "GET":
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data["subject"]
            from_email = form.cleaned_data["from_email"]
            message = form.cleaned_data['message']
            send_mail(subject, message, from_email, ["admin@example.com"])
    template = loader.get_template('contact.html')
    return HttpResponse(template.render({"form": form}), request))

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