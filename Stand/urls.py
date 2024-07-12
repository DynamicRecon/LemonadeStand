from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="Home"),
    path("OpenForBusiness", views.open, name="Open"),
    path("ClosedForBusiness", views.close, name="Close")
]
