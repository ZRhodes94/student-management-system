from django.db import models

# Create your models here.
class Teacher(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    room = models.IntegerField()

    def __str__(self):
        return self.name

class Course(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    time = models.TimeField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    gradeLevel = models.IntegerField()
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name

class Parent(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    students = models.ManyToManyField(Student)

    def __str__(self):
        return self.name

class Behavior(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    description = models.TextField()
    interventions = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE, default=0)

class Assignment(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    name = models.CharField(max_length=80)
    description = models.TextField()
    pointsPossible = models.IntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.name

class Grade(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    pointsEarned = models.IntegerField()
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, default=0)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,  default=0)