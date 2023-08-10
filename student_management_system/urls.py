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
]