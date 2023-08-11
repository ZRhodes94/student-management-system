from django.urls import path

from . import views

urlpatterns = [
    path("", views.login_view, name="login"),
    path("home/", views.home_view, name="home_view"),
    path("class/<int:id>", views.class_view, name="class_view"),
    path("behavior/", views.behavior_view, name="behavior_view"),
    path("assignments/", views.assignments_view, name="assignments_view"),
    path("assignments/delete/<int:id>", views.delete_assignment, name="delete_assignments_view"),
    path("behavior/delete/<int:id>", views.delete_behavior, name="delete_behavior_view"),
    path("class/<int:course_id>/grade/delete/<int:grade_id>", views.delete_grade, name="delete_grade_view"),
    path("assignments/edit/<int:id>", views.edit_assignment, name="edit_assignments_view"),
    path("behavior/edit/<int:id>", views.edit_behavior, name="edit_behavior_view"),
    path("class/<int:course_id>/grade/edit/<int:grade_id>", views.edit_grade, name="edit_grade_view"),
    path('assignment/updaterecord/<int:id>', views.updaterecord_assignment, name='updaterecord_assignment'),
    path('behavior/updaterecord/<int:id>', views.updaterecord_behavior, name='updaterecord_behavior'),
    path('class/<int:course_id>/grade/updaterecord/<int:grade_id>', views.updaterecord_behavior, name='updaterecord_grade'),
    
]