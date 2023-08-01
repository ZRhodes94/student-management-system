from django.db import models

# Create your models here.
class Teacher(models.Model):
    teacherID = models.IntegerField()
    name = models.CharField(max_length=80)
    room = models.IntegerField()

class Student(models.Model):
    studentID = models.IntegerField()
    name = models.CharField(max_length=80)
    gradeLevel = models.IntegerField()

class Parent(models.Model):
    parentID = models.IntegerField()
    name = models.CharField(max_length=80)
    studentID = models.IntegerField()

class Behavior(models.Model):
    behaviorID = models.IntegerField()
    description = models.CharField()
    interventions = models.CharField()
    studentID = models.IntegerField()

class Course(models.Model):
    courseID = models.IntegerField()
    name = models.CharField(max_length=80)
    description = models.CharField()
    time = models.IntegerField()
    teacherID = models.IntegerField()

class Assignment(models.Model):
    assignmentID = models.IntegerField()
    name = models.CharField(max_length=80)
    description = models.CharField()
    pointsPossible = models.IntegerField()
    courseID = models.IntegerField()

class Student_Courses(models.Model):
    studentID = models.IntegerField()
    courseID = models.IntegerField()

class Grades(models.Model):
    assignmentID = models.IntegerField()
    studentID = models.IntegerField()
    courseID = models.IntegerField()
    pointsEarned = models.IntegerField()

