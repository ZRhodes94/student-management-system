from django.contrib import admin
from .models import Teacher, Student, Parent, Assignment, Grade, Behavior, Course

# Register your models here.
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(Assignment)
admin.site.register(Grade)
admin.site.register(Behavior)
admin.site.register(Course)

