from django.db import models
import datetime

# Create your models here.
class Teacher(models.Model):
    name = models.CharField(max_length=80)
    room = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=80)
    description = models.TextField()
    time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name + " (" + self.time.strftime("%H:%M") + ")- " + self.teacher.name

class Student(models.Model):
    name = models.CharField(max_length=80)
    gradeLevel = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Parent(models.Model):
    name = models.CharField(max_length=80)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

class Behavior(models.Model):
    description = models.TextField()
    interventions = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)
    date = models.DateField(default=datetime.date.today)

class Assignment(models.Model):
    name = models.CharField(max_length=80)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)
    dueDate = models.DateField(default=datetime.date.today)
    pointsPossible = models.IntegerField()
    description = models.TextField()


    def __str__(self):
        return self.name

class Grade(models.Model):
    pointsEarned = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  default=0)